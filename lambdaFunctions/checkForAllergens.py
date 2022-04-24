import json
import boto3

def lambda_handler(event, context):
    try:
        dynamodb = boto3.client('dynamodb')
        db = boto3.resource('dynamodb')
        allergenInfoTable = db.Table('allergenInfo')
        rekognitionItems = db.Table('detectedText')
        
        knownFoodAllergens = allergenInfoTable.scan(AttributesToGet=['food'])
        foodList = list(knownFoodAllergens.values())
        k = [x['food'] for x in foodList[0]]
        known = [x.lower() for x in k]
        
        detectedIngredients = rekognitionItems.scan(AttributesToGet=['ingredientList'])
        detectedList = list(detectedIngredients.values())
        d = list(detectedList[0][0]['ingredientList'])
        detected = [x.lower() for x in d]
        
        match = list(set(known).intersection(detected))
        if len(match) == 0:
            return False
        else:
            print(match)
            return match

    except Exception as e: 
        print(str(e))
    
