from ec2_operations import (
    list_instances,
    start_instance,
    stop_instace,
    terminate_instance,
    get_instance_details
)


while True:
    print("\nAWS EC2 Manager")

    print("1. List Instances")
    print("2. Start Instance")
    print("3. Stop Instance")
    print("4. Terminate Instance")
    print("5: View Instance Details")
    print("6: View Log file")
    print("7. Exit")

    Choice = input("Enter Choice: ")
    #List the instances
    if Choice == "1":
        #call function to list instances
        list_instances()

    #Start Instances
    elif Choice == "2":
        print("If you want start more than one instance use space or comma: EC2-ID1,EC2ID2 or EC2-ID1 EC2-ID2")
        instance_id_input = input("Enter Instance Id:- ")
        instance_id = None

        if ',' in instance_id_input:
            instance_id = instance_id_input.split(',')
        else:
            instance_id = instance_id_input.split()

        #Call function to start instance
        start_instance(instance_id)

    #Stop instances
    elif Choice == "3":
        print("If you want stop more than one instance use space or comma: EC2-ID1,EC2ID2 or EC2-ID1 EC2-ID2")
        instance_id_input = input("Enter Instance Id:- ")
        instance_id = None

        if ',' in instance_id_input:
            instance_id = instance_id_input.split(',')
        else:
            instance_id = instance_id_input.split()

        #Call function to stop instance
        stop_instace(instance_id)
    
    #Terminate Instances
    elif Choice == "4":
        print("If you want terminate more than one instance use space or comma: EC2-ID1,EC2ID2 or EC2-ID1 EC2-ID2")
        instance_id_input = input("Enter Instance Id:- ")
        instance_id = None

        if ',' in instance_id_input:
            instance_id = instance_id_input.split(',')
        else:
            instance_id = instance_id_input.split()

        #Call function to terminate instance
        terminate_instance(instance_id)

    #Get Instance details
    elif Choice == "5":
        print("If you want terminate more than one instance use space or comma: EC2-ID1,EC2ID2 or EC2-ID1 EC2-ID2")
        instance_id_input = input("Enter Instance Id:- ")
        instance_id = None

        if ',' in instance_id_input:
            instance_id = instance_id_input.split(',')
        else:
            instance_id = instance_id_input.split()
        
        #Call function to fetch instance details
        get_instance_details(tuple(instance_id))

    #Read Log files 
    elif Choice == "6":
        with open('logs/aws_manager.log','r') as f:
            for i in f.readlines():
                print(i)
    
    #Break the loop
    elif Choice == "7":
        break
    else:
        print("Choose valid choise 1 to 4.")
