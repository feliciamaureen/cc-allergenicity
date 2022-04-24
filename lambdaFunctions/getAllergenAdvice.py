import json
import boto3

def lambda_handler(event, context):
    try:
        dynamo = boto3.resource('dynamodb')
        table = dynamo.Table('cc-info')
    
        response = table.get_item(
            Key={
                'ID': '1'
            }
        )
    
        return response['Item'].get('infoVal')

    except Exception as e: 
        print(str(e))
    