import joblib

from flask import Flask, request
import json
import numpy as np
from pymongo import MongoClient
from pprint import pprint

app = Flask(__name__)

model = joblib.load('model.joblib')
client = MongoClient(
    "mongodb+srv://minanicola:indoortrackingsystem@cluster0.up86c.mongodb.net/its?retryWrites=true&w=majority")
db = client.its


@app.route('/predict', methods=['POST'])
def predict():
    event = json.loads(request.data)
    data = event["data"]
    pre = np.array(data)
    pre = pre.reshape(1, -1)
    predictedSquare = model.predict(pre)[0]
    pixelSquare = db.squares.find_one({'name': predictedSquare})
    del pixelSquare['_id']
    return json.dumps(pixelSquare, separators=(',', ':'))


if __name__ == '__main__':
    app.run()
