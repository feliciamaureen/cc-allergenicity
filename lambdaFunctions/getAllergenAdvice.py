import json
import boto3

def lambda_handler(event, context):
    try:
        dynamo = boto3.resource('dynamodb')
        table = dynamo.Table('cc-info')
    
        advice = table.scan(AttributesToGet=['infoVal'])
        adviceList = list(advice.values())
        a = list(adviceList[0])
        allAdvice = [d['infoVal'] for d in a]

        return allAdvice

    except Exception as e: 
        print(str(e))
    