import json
import json
import boto3
import re

def lambda_handler(event, context):
    region = 'us-east-1'
    
    try:
        rekognition = boto3.client("rekognition", region_name = region)
        dynamodb = boto3.client('dynamodb', region_name = region)
        s3 = boto3.client('s3')
        
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = event['Records'][0]['s3']['object']['key']
        
        response = rekognition.detect_text(Image = {"S3Object": {"Bucket": bucket, "Name": key}})
        textDetections = response['TextDetections']
        detectedText = []
        detectedImageID = 0

        for text in textDetections:
            strip = re.sub("[^a-zA-Z]+", " ", text['DetectedText']).strip()
            detectedText.append(strip)
        detectedText = list(dict.fromkeys(detectedText))
        
        add_to_db = dynamodb.put_item(
                TableName = 'detectedText',
                Item = {
                    'detectedImageID' : {'N': str(detectedImageID)},
                    'imageName' : {'S': str(key)},
                    'ingredientList' : {'SS': detectedText}
                })
        detectedImageID = detectedImageID + 1
        
        return True
        
    except Exception as e: 
        print(str(e))
