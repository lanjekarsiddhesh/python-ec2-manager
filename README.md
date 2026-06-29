# Python EC2 Manager

A simple Python CLI application to manage AWS EC2 instances using Boto3.

This project was built primarily to understand Python decorators by implementing authentication checks, centralized logging, and exception handling while interacting with AWS EC2 instances.

---

## Features

- List all EC2 instances
- Start EC2 instances
- Stop EC2 instances
- Terminate EC2 instances
- Fetch EC2 instance details
- Chcek authentication using decorators
- Exception handling using decorators
- Logging every operation into log files
- Clean and modular code structure

---

## Technologies Used

- Python 3.10.12
- Boto3
- AWS EC2
- Logging Module
- Python Decorators

---

## Project Structure

```
AWS-EC2-Manager/
    auth.py
    decorators.py
    ec2_operations.py
    StoreLog.py
    main.py
    requirements.txt

    logs/
      aws_manager.log
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/lanjekarsiddhesh/python-ec2-manager.git
```

Go to project directory

```bash
cd python-ec2-manager
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Configure AWS Credentials

Configure your AWS credentials using the AWS CLI.

```bash
aws configure
```

Provide:

- AWS Access Key
- AWS Secret Key
- Region
- Output Format

---

## Run

```bash
python AWS-EC2-Manager/main.py
```

---

## Example Menu

```
1. List Instances
2. Start Instance
3. Stop Instance
4. Terminate Instance
5: View Instance Details
6: View Log file
7. Exit
```

---

## Screenshots

### List Instances
<img width="973" height="755" alt="image" src="https://github.com/user-attachments/assets/96a52012-df81-4e86-8016-7c209aa7322b" />

### Stop Instance
<img width="1000" height="829" alt="image" src="https://github.com/user-attachments/assets/fb9db582-b435-46cb-adea-deccaafd6563" />

### Start Instance
<img width="962" height="908" alt="image" src="https://github.com/user-attachments/assets/218f30b4-6e22-4e68-b276-ab79a6c34934" />

### Intance Details
<img width="980" height="580" alt="image" src="https://github.com/user-attachments/assets/8775119f-edb2-4d2b-8dd5-1f8217474d01" />

### Terminate Insatnce
<img width="976" height="697" alt="image" src="https://github.com/user-attachments/assets/a39d13d2-b53e-4cf3-8fd0-8d38205b8fe5" />

### Logs
<img width="973" height="755" alt="image" src="https://github.com/user-attachments/assets/7dac9113-f085-4155-bd3d-1118232bb4a1" />

---

## Future Improvements

- IAM User Authentication
- Multi-region support
- Create/Delete EC2 Instances
- EC2 Tag Management
- Security Group Management
- EBS Volume Management
- CLI arguments using argparse
- Unit Testing
- Docker Support

---

## Learning Outcomes

Through this project, we learned:

- Python decorators
- Function wrapping
- Authentication decorators
- Exception handling
- Logging
- AWS EC2 management using Boto3
- Modular project architecture
- Clean code practices

---
