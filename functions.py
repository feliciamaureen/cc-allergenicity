import boto3
import json
import re
import requests
from config import *

#Query dynamodb for allergen advice 
def getAdviceAPIGateway():
    r = requests.get('https://fyo4xgtvib.execute-api.us-east-1.amazonaws.com/test')
    return r.text

#detect text in uploaded image with rekognition, send tokens to dynamo
def rekognitionAddToDynamo():
    client = lambdaCredentials()
    test_event = dict()
    resp = client.invoke(
        FunctionName = 'getAllergensRekognition',
        Payload = json.dumps(test_event)
    )

#get list of ingredients from rekognition
def returnTokens():
    client = lambdaCredentials()
    test_event = dict()
    resp = client.invoke(
        FunctionName = 'getTokensRekognition',
        Payload = json.dumps(test_event)
    )

    rTokens = resp['Payload'].read().decode("utf-8")
    strip = re.sub("[^a-zA-Z]+", " ", rTokens).strip()
    tokenList = strip.split(' ')
    return tokenList


#get matched ingredients based on uploaded image
def returnMatches():
    client = lambdaCredentials()
    test_event = dict()
    resp = client.invoke(
        FunctionName = 'checkForAllergens',
        Payload = json.dumps(test_event)
    )
    matches = resp['Payload'].read().decode("utf-8")
    strip = re.sub("[^a-zA-Z]+", " ", matches).strip()
    matchList = strip.split(' ')
    
    return matchList
