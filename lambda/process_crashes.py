import boto3

s3 = boto3.client('s3')
response = s3.list_objects_v2(Bucket ="chicago-crash-data-pipeline-taufeeq")
# print(response)

file_key = None

for obj in response["Contents"]:
    if obj["Key"] == "raw/traffic-crashes.csv":
        file_key = obj["Key"]

# print(file_key)

response = s3.get_object(
    Bucket="chicago-crash-data-pipeline-taufeeq",
    Key=file_key
)

# print(response)

body = response["Body"].read(2000)
body = body.decode('utf-8')
print(body)