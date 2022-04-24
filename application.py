import logging
import boto3
import os
import requests
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from botocore.exceptions import ClientError

from config import *
from functions import *

app = Flask(__name__)
app.secret_key = b'secretKey'

@app.route('/')
def home():
    #Call Lambda function getAllergenAdvice - shows content from DynamoDB
    advice = getAdviceAPIGateway()

    #call lambda function to show allergen stats 
    return render_template("application.html", advice = advice)

@app.route('/upload',methods=['post'])
def upload():
    #Upload user image to S3 bucket
    s3Client = s3Credentials()
    BUCKET_NAME='allergenicity-useruploads'
    if request.method == 'POST':
        img = request.files['file']
        if img:
                filename = secure_filename(img.filename)
                img.save(filename)
                s3Client.upload_file(
                    Bucket = BUCKET_NAME,
                    Filename=filename,
                    Key = filename
                )
                uploaded = True
    #Call Lambda function getAllergensRekognition to extract text from uploaded image
    tokenise = rekognitionAddToDynamo()

    return redirect(url_for('result'))
    #return render_template("application.html")

@app.route('/result')
def result():
    #Call Lambda function getTokensRekognition to extracted text from Rekognition
    tokens = returnTokens()

    #Call Lambda function checkForAllergens to get tokens recognised as allergens
    matches = returnMatches()
    if matches is not True:
        flash('no allergens')
    
    return render_template("results.html", tokens = tokens, matches = matches)

if __name__ == "__main__":
    app.debug = True
    app.run()
