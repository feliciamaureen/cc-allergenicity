import json
import boto3

def lambda_handler(event, context):
    try:
        dynamo = boto3.resource('dynamodb')
        rekognitionItems = dynamo.Table('detectedText')
        
        detectedIngredients = rekognitionItems.scan(AttributesToGet=['ingredientList'])
        detectedList = list(detectedIngredients.values())
        d = list(detectedList[0][0]['ingredientList'])
        detected = [x.lower() for x in d]
        return detected

    except Exception as e: 
        print(str(e))
    