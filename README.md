How to run:

1. Make sure you have Python installed on your system and that it's accessible from the command line. 

2. bash cd path/to/directory

3. python main.py

Result:

![image](https://github.com/LukaszKrolicki/AWS-IAM-Role-JSON-verification/assets/54467678/2b1c64b6-8d21-466f-aff5-985c22f928bc)


--------------------------------------

Method shall return logical false if an input JSON Resource field contains a single asterisk and true in any other case. 

Verifying the input JSON data:

https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-role-policy.html

------------------------------------------

Example of JSON:

![image](https://github.com/LukaszKrolicki/AWS-IAM-Role-JSON-verification/assets/54467678/128e6db8-20f3-4098-99cd-5349ded1e884)

-------------------------------------------

Requirements:

![image](https://github.com/LukaszKrolicki/AWS-IAM-Role-JSON-verification/assets/54467678/a6ba03f0-ce91-4a58-a049-e9012e0ca98f)

![image](https://github.com/LukaszKrolicki/AWS-IAM-Role-JSON-verification/assets/54467678/893341d0-c619-4867-b845-68db7da089a8)

More detailed:

![image](https://github.com/LukaszKrolicki/AWS-IAM-Role-JSON-verification/assets/54467678/0b2aa084-f53c-454b-bbad-3cd26b50b8d5)

![image](https://github.com/LukaszKrolicki/AWS-IAM-Role-JSON-verification/assets/54467678/9b544e6e-b8e1-4d78-9280-64bc9226215a)

------------------------------------------

amzaon.json - json file that contains JSON to be checked

![image](https://github.com/LukaszKrolicki/AWS-IAM-Role-JSON-verification/assets/54467678/d43682e2-7255-4019-a3de-e7c5e348b5b3)

-------------------------------------------

main.py

reading json file, setting validation flag (If wrong formatted validation_flag = False ,  if properly formatted and single asterisk validation_flag=True_):

![image](https://github.com/LukaszKrolicki/AWS-IAM-Role-JSON-verification/assets/54467678/a8344c00-c574-4850-b3ee-3711a0508b61)

checking if policy_name meets the requirements:

![image](https://github.com/LukaszKrolicki/AWS-IAM-Role-JSON-verification/assets/54467678/c80a1a69-b4b6-4f33-af28-36a6cb314293)

checking if policy_document meets the requirements:
![image](https://github.com/LukaszKrolicki/AWS-IAM-Role-JSON-verification/assets/54467678/dd3d0170-6522-45f0-8513-e8a34b1379ab)

solution returns False if everything properly formatted and one asterisk in source and True when resource doesnt have single asterisk or is wrongly formatted

![image](https://github.com/LukaszKrolicki/AWS-IAM-Role-JSON-verification/assets/54467678/08f80ca4-07e6-4cc0-b0ba-2f95b4de1b5a)

----------------------------------------------------------

Tests

![image](https://github.com/LukaszKrolicki/AWS-IAM-Role-JSON-verification/assets/54467678/6981c8fc-156d-4c2e-b1e2-e52970bf4c0b)

setup:

![image](https://github.com/LukaszKrolicki/AWS-IAM-Role-JSON-verification/assets/54467678/0a921fea-9aa1-4426-baa2-de206a40e1ef)

valid Test:

![image](https://github.com/LukaszKrolicki/AWS-IAM-Role-JSON-verification/assets/54467678/0be9eaed-b051-4407-b20b-07dd38549cbf)

policy_name Tests with edge cases:

![image](https://github.com/LukaszKrolicki/AWS-IAM-Role-JSON-verification/assets/54467678/f5a79564-c5a5-40d0-a5e7-63782fc531bd)

policy_doucments Tests with edge cases:

![image](https://github.com/LukaszKrolicki/AWS-IAM-Role-JSON-verification/assets/54467678/7d76ab10-7509-4aa8-9e3b-fd9d98f05833)

![image](https://github.com/LukaszKrolicki/AWS-IAM-Role-JSON-verification/assets/54467678/83d1bdbd-c033-4cb7-862f-370aac517ac7)

----------------------------------------------------------

Result with properly formatted json

![image](https://github.com/LukaszKrolicki/AWS-IAM-Role-JSON-verification/assets/54467678/e68ae1e6-50eb-43c9-8d4a-728a98a5498f)\

Result with wrongly formatted json

![image](https://github.com/LukaszKrolicki/AWS-IAM-Role-JSON-verification/assets/54467678/f29634a5-b5ee-41ae-95e5-9f07d9c26b09)




