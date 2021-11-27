from fastapi import FastAPI, Path, Query
from typing import Optional
from pydantic import BaseModel
import tensorflow as tf
import tensorflow_text
import numpy as np
import boto3
import os

ACCESS_KEY_ID = 'xxxx'
SECRET_KEY = 'xxxx'

def downloadDirectoryFroms3(bucketName, remoteDirectoryName):
    s3_resource = boto3.resource('s3', aws_access_key_id=ACCESS_KEY_ID, aws_secret_access_key=SECRET_KEY)
    bucket = s3_resource.Bucket(bucketName) 
    for obj in bucket.objects.filter(Prefix = remoteDirectoryName):
        if not os.path.exists(os.path.dirname(obj.key)):
            os.makedirs(os.path.dirname(obj.key))
        bucket.download_file(obj.key, obj.key)

downloadDirectoryFroms3('modelo-bert-amazon-eacd', 'amazon_bert')


app = FastAPI()
model = tf.keras.models.load_model('amazon_bert')
#s3://modelo-bert-amazon-eacd/amazon_bert

@app.post("/predict")
def predict_sentiment(review: str):
    x = np.array([review])
    y_predicted = float(model.predict(x).reshape(-1)[0])
    if y_predicted >= 0.5:
        result = 'Positive'
    elif y_predicted < 0.5:
        result = 'Negative'
    return {"Sentiment":result, "Score": y_predicted}
