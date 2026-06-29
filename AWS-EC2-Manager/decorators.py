import time
from functools import wraps
from auth import verify_aws_login
import boto3
from StoreLog import store_log

#chcek login
def required_aws_login(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if not verify_aws_login():
            store_log(Msg="AWS Authentication Failed !!!", level="error")
            print("AWS Authentication Failed !!!")
        return func(*args, **kwargs)
    return wrapper

#chcek active user
def AWSIamUser(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        iam = boto3.client("iam")
        response = iam.get_user()
        result = func(*args,**kwargs)
        store_log(Msg=f'Active User: {response["User"]["UserName"]}')
        print(f'Active User: {response["User"]["UserName"]}')
        return result
    return wrapper

#Save log in to the file
def logger(func):
    @AWSIamUser
    @wraps(func)
    def wrapper(*args,**kwargs):
        store_log(Msg=f"Running {func.__name__}")
        result = func(*args,**kwargs)
        store_log(Msg=f"Completed {func.__name__}")
        return result
    return wrapper

def timer(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f"[TIME] {func.__name__} took {end-start:.2f} sec")
        return result
    return wrapper


#retry decorator if API fail due to temp network issue.
def retry(max_attempt=3, delay=3):
    def decorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            for attempt in range(max_attempt):
                try:
                    return func(*args,**kwargs)
                except Exception as e:
                    store_log(Msg=f'Attempt {attempt+1} failed',level='warn')
                    print(f'Attempt {attempt+1} failed')
                    if attempt == max_attempt -1:
                        raise 
                    time.sleep(delay)
        return wrapper
    return decorator

