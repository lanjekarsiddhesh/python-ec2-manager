import boto3
import secrets, string
from decorators import logger, timer, required_aws_login,retry
from functools import lru_cache
from botocore.exceptions import ClientError
from StoreLog import store_log


ec2 = boto3.client("ec2")

def generate_confirmation_code():
    """Generate a secure , 5 digit  confirmation code string"""
    alphabet = string.ascii_uppercase + string.digits + string.ascii_lowercase
    return ''.join(secrets.choice(alphabet) for _ in range(7))

#List Instances
@required_aws_login
@retry(max_attempt=3)
@logger
@timer
def list_instances():
    response = ec2.describe_instances()

    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            store_log(Msg=f"List the instances:- {instance}")
            print(f"ID: {instance['InstanceId']}")
            print(f"State: {instance['State']['Name']}")
            if instance['State']['Name'] != 'terminated':
                if instance['State']['Name'] != 'shutting-down':
                    print(f"Private IP: {instance['NetworkInterfaces'][0]['PrivateIpAddress']}")
                    print(f"Private DNS: {instance['NetworkInterfaces'][0]['PrivateDnsName']}")
                    print(f"MAC Address: {instance['NetworkInterfaces'][0]['MacAddress']}")
            print("-"*30)

#Start Instances
@required_aws_login
@retry(max_attempt=3)
@logger
@timer
def start_instance(instance_id):
    for id in instance_id:
        try:
            ec2.start_instances(InstanceIds=[id])
            #Store logs
            store_log(Msg=f"Starting {id}")
            print(f"Starting {id}")
        except ClientError as e:
            #Store logs
            store_log(Msg=e.response["Error"]["Message"],level="error")
            print(e.response["Error"]["Message"])            

#stop Instance
@required_aws_login
@retry(max_attempt=3)
@logger
@timer
def stop_instace(instance_id):
    for id in instance_id:
        try:
            ec2.stop_instances(InstanceIds=[id])
            #Store logs
            store_log(Msg=f"stopping {id}")
            print(f"stopping {id}")
        except ClientError as e:
            #Store logs
            store_log(Msg=e.response["Error"]["Message"],level="error")
            print(e.response["Error"]["Message"]) 

@required_aws_login
@retry(max_attempt=3)
@logger
@timer
def terminate_instance(instance_id):
    code = generate_confirmation_code()

    Confirmation = input(f"Please Type:- {code} to terminate selected instances: ")

    if Confirmation == code:
        for id in instance_id:
            try:
                ec2.terminate_instances(InstanceIds=[id])
                #Store in log file
                store_log(Msg=f"Terminated: {id}")
                print(f"Terminated: {id}")
            except ClientError as e:
                #Store logs
                store_log(Msg=e.response["Error"]["Message"],level="error")
                print(e.response["Error"]["Message"]) 
    else:
        #Store logs
        store_log(Msg="Enter wrong verification code so instances are not terminated.",level="warn")
        print("You enter wrong code so instances are not terminated.")


@logger
@timer
@lru_cache(maxsize=32)
def get_instance_details(instance_id):
    for id in instance_id:
        try:
            response = ec2.describe_instances(InstanceIds=[id])
            instance =  response["Reservations"][0]["Instances"][0]
            details = {
                "Instance ID": instance["InstanceId"],
                "State": instance["State"]["Name"],
                "Instance Type": instance["InstanceType"],
                "Availability Zone": instance["Placement"]["AvailabilityZone"],
                "Private IP": instance.get('PrivateIpAddress'),
                "Launch Time": str(instance["LaunchTime"]),
            }
            if details:
                #Store logs
                store_log(Msg=f"Fetching infoemation of EC2 instance ({id}) is successfully")
                store_log(Msg=f"result: {details}")
                print("\nEC2 Instnace Details")
                print('-'*40)
                for key,Value in details.items():
                    print(f"{key:20}:{Value}")
                    
        except ClientError as e:
            #Store logs
            store_log(Msg=e.response["Error"]["Message"],level="error")
            print(f"AWS Error: {e.response['Error']['Message']}")
            return None
        
        except IndexError:
            #Store logs
            store_log(Msg="Instance not found.",level="warn")
            print("Instance not found.")
            return None