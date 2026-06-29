#Before any AWS operation validate AWS credentials
import boto3
from botocore.exceptions import ClientError, NoCredentialsError

def verify_aws_login():
    try:
        sts = boto3.client("sts")
        sts.get_caller_identity()
        return True
    except (NoCredentialsError, ClientError):
        return False