import boto3
import json
from recursive_diff import recursive_diff
s3 = boto3.resource(
    service_name='s3',
    region_name='ap-south-1',
    aws_access_key_id='',
    aws_secret_access_key=''
)

obj = s3.Bucket('readfroms3').Object('test1.json').get()['Body'].read().decode('utf-8')
test1 = json.loads(obj)
obj2 = s3.Bucket('readfroms3').Object('test2.json').get()['Body'].read().decode('utf-8')
test2 = json.loads(obj2)
for diff in recursive_diff(test1, test2, abs_tol=.1):
    print(diff)
