import boto3, botocore

def s3Credentials():
    s3 = boto3.client(
        service_name = 's3',
        region_name = 'us-east-1',
        aws_access_key_id = 'ASIAWUVGNFBZY33QLOMT',
        aws_secret_access_key = '4QS8eU7KsQ8bG8y+3WUtHLS0B9XNFdqjo/XB7Vo/',
        aws_session_token = 'FwoGZXIvYXdzENP//////////wEaDJzRpUgj7lKiMUBFiCLMAQJbt+YsBE1mfEV6NSOgAm3jehNRlgII15MyZXyx5vV+BaZFbIvvsXEn0uCboLtOhoS94WPeEaUtHUBFPWuQ/lGgFXzKWvSZiasFZwS2ocgdQ1TCrOjSyl2lW/poXbfFg4YiVvQpiFJ7kJzRXzRmrSHA7AbUlrsRQ77QCNe9ePVIRUoZQEo+uKpKydGyKAIAsFaqpyA7Gf1O6ALHkYjvIdk31zF34azr8rnSEwv8iouzAtsWtzSOWfVzcy2MDygcxcc7aJrrb0+ZcGLHjSiAmZaTBjItOpkJjhO1sGiOMYIa+NVhycf5uCkBjYk8JGpcfuKKR0PCMfSi508hf7PzOMO0'
    )
    return s3

def dynamoCredentials():
    dynamodb = boto3.client(
        service_name = 'dynamodb',
        region_name = 'us-east-1',
        aws_access_key_id = 'ASIAWUVGNFBZY33QLOMT',
        aws_secret_access_key = '4QS8eU7KsQ8bG8y+3WUtHLS0B9XNFdqjo/XB7Vo/',
        aws_session_token = 'FwoGZXIvYXdzENP//////////wEaDJzRpUgj7lKiMUBFiCLMAQJbt+YsBE1mfEV6NSOgAm3jehNRlgII15MyZXyx5vV+BaZFbIvvsXEn0uCboLtOhoS94WPeEaUtHUBFPWuQ/lGgFXzKWvSZiasFZwS2ocgdQ1TCrOjSyl2lW/poXbfFg4YiVvQpiFJ7kJzRXzRmrSHA7AbUlrsRQ77QCNe9ePVIRUoZQEo+uKpKydGyKAIAsFaqpyA7Gf1O6ALHkYjvIdk31zF34azr8rnSEwv8iouzAtsWtzSOWfVzcy2MDygcxcc7aJrrb0+ZcGLHjSiAmZaTBjItOpkJjhO1sGiOMYIa+NVhycf5uCkBjYk8JGpcfuKKR0PCMfSi508hf7PzOMO0'
    )
    return dynamodb

def lambdaCredentials():
    awsLambda = boto3.client(
        service_name = 'lambda',
        region_name = 'us-east-1',
        aws_access_key_id = 'ASIAWUVGNFBZY33QLOMT',
        aws_secret_access_key = '4QS8eU7KsQ8bG8y+3WUtHLS0B9XNFdqjo/XB7Vo/',
        aws_session_token = 'FwoGZXIvYXdzENP//////////wEaDJzRpUgj7lKiMUBFiCLMAQJbt+YsBE1mfEV6NSOgAm3jehNRlgII15MyZXyx5vV+BaZFbIvvsXEn0uCboLtOhoS94WPeEaUtHUBFPWuQ/lGgFXzKWvSZiasFZwS2ocgdQ1TCrOjSyl2lW/poXbfFg4YiVvQpiFJ7kJzRXzRmrSHA7AbUlrsRQ77QCNe9ePVIRUoZQEo+uKpKydGyKAIAsFaqpyA7Gf1O6ALHkYjvIdk31zF34azr8rnSEwv8iouzAtsWtzSOWfVzcy2MDygcxcc7aJrrb0+ZcGLHjSiAmZaTBjItOpkJjhO1sGiOMYIa+NVhycf5uCkBjYk8JGpcfuKKR0PCMfSi508hf7PzOMO0'
    )
    return awsLambda
