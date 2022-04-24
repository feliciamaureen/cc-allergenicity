import json
import csv
import boto3

def lambda_handler(event, context):
    region = 'us-east-1'
    dataList = []
    
    try:
        s3 = boto3.client('s3')
        dynamodb = boto3.client('dynamodb', region_name = region)
        
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = event['Records'][0]['s3']['object']['key']
        
        csvFile = s3.get_object(Bucket = bucket, Key = key)
        dataList = csvFile['Body'].read().decode('utf-8').split('\n')
        csv_reader = csv.reader(dataList, delimiter = ',', quotechar = '"')
        allergenID = 0
        
        for row in csv_reader:
            allergenClass = row[0]
            allergenType = row[1]
            allergenGroup = row[2]
            food = row[3]
            allergy = row[4]

            add_to_db = dynamodb.put_item(
                TableName = 'allergenInfo',
                Item = {
                    'allergenID' : {'N': str(allergenID)},
                    'allergenClass' : {'S': str(allergenClass)},
                    'allergenType' : {'S': str(allergenType)},
                    'allergenGroup' : {'S': str(allergenGroup)},
                    'food' : {'S': str(food)},
                    'allergy' : {'S': str(allergy)}
                })
            allergenID = allergenID + 1
            
        print('success add')
            
    except Exception as e: 
        print(str(e))
        
    return {
        'statusCode': 200,
        'body': json.dumps('success!')
    }
