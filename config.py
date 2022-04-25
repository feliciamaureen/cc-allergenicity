import boto3, botocore

def s3Credentials():
    s3 = boto3.client(
        service_name = 's3',
        region_name = 'us-east-1',
        aws_access_key_id = 'ASIAWUVGNFBZ2IR5RYF3',
        aws_secret_access_key = 'T2hsv3oKXqQaRM1dgxa9j2X+zYMKPNn8Eaq8girc',
        aws_session_token = 'FwoGZXIvYXdzEN///////////wEaDIviZKOVdaD1pssi4yLMAfseNhZP79jaEHy1BgRYID9UtB+sVrJLTZlgCe7IRZrWLV9yliHlNmQx7jnSQXJ8BUh8u1Vrx97ERMqeK1Rqzx7n0LYWCT8HblCbwAl7ASKjH5F+mj+Pp17hs7Vfx2kEq/ue6FAJQXY7VHyBeCvTs0ldHd0/Orl/vz95uvx00IK7kSzypE37/W72DzxpoDLuq3eRIe/lz6v9V7JWC1sSa+1euHb22R2bS0y7/m6yfA9pRoAsAK/zL+iNT5oY4/0Bcd4UEXHICP+ZxVPISCjV6JiTBjIto8vLNs+h3SrEwAr+eMswtF1O1EyA6mJb57NjFhnpJtCq9K6DuaBfKCQ/0mhn'
    )
    return s3

def dynamoCredentials():
    dynamodb = boto3.client(
        service_name = 'dynamodb',
        region_name = 'us-east-1',
        aws_access_key_id = 'ASIAWUVGNFBZ2IR5RYF3',
        aws_secret_access_key = 'T2hsv3oKXqQaRM1dgxa9j2X+zYMKPNn8Eaq8girc',
        aws_session_token = 'FwoGZXIvYXdzEN///////////wEaDIviZKOVdaD1pssi4yLMAfseNhZP79jaEHy1BgRYID9UtB+sVrJLTZlgCe7IRZrWLV9yliHlNmQx7jnSQXJ8BUh8u1Vrx97ERMqeK1Rqzx7n0LYWCT8HblCbwAl7ASKjH5F+mj+Pp17hs7Vfx2kEq/ue6FAJQXY7VHyBeCvTs0ldHd0/Orl/vz95uvx00IK7kSzypE37/W72DzxpoDLuq3eRIe/lz6v9V7JWC1sSa+1euHb22R2bS0y7/m6yfA9pRoAsAK/zL+iNT5oY4/0Bcd4UEXHICP+ZxVPISCjV6JiTBjIto8vLNs+h3SrEwAr+eMswtF1O1EyA6mJb57NjFhnpJtCq9K6DuaBfKCQ/0mhn'
    )
    return dynamodb

def lambdaCredentials():
    awsLambda = boto3.client(
        service_name = 'lambda',
        region_name = 'us-east-1',
        aws_access_key_id = 'ASIAWUVGNFBZ2IR5RYF3',
        aws_secret_access_key = 'T2hsv3oKXqQaRM1dgxa9j2X+zYMKPNn8Eaq8girc',
        aws_session_token = 'FwoGZXIvYXdzEN///////////wEaDIviZKOVdaD1pssi4yLMAfseNhZP79jaEHy1BgRYID9UtB+sVrJLTZlgCe7IRZrWLV9yliHlNmQx7jnSQXJ8BUh8u1Vrx97ERMqeK1Rqzx7n0LYWCT8HblCbwAl7ASKjH5F+mj+Pp17hs7Vfx2kEq/ue6FAJQXY7VHyBeCvTs0ldHd0/Orl/vz95uvx00IK7kSzypE37/W72DzxpoDLuq3eRIe/lz6v9V7JWC1sSa+1euHb22R2bS0y7/m6yfA9pRoAsAK/zL+iNT5oY4/0Bcd4UEXHICP+ZxVPISCjV6JiTBjIto8vLNs+h3SrEwAr+eMswtF1O1EyA6mJb57NjFhnpJtCq9K6DuaBfKCQ/0mhn'
    )
    return awsLambda