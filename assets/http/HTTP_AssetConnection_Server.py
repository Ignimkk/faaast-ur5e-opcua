#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask, request
from flask_api import status
app = Flask(__name__)

value = 42

@app.route('/value', methods = ['GET']) 
def getValue():
    return json.dumps({'value': value}), status.HTTP_200_OK

@app.route('/value', methods = ['PUT'])
def writeValue():
    global value
    updatedValue = float(request.json['value'])
    print("Receive new value: " + str(updatedValue))
    value = updatedValue
    return "Update value with " + str(updatedValue), status.HTTP_200_OK

@app.route('/add', methods = ['POST'])
def add():
    global value
    input1 = float(request.json['data']['input1'])
    input2 = float(request.json['data']['input2'])
    print(str(input1) + "+" + str(input2))
    value = value + input1 + input2
    return  json.dumps({'result': str(value)}), status.HTTP_200_OK

if __name__ == "__main__":
    app.run('0.0.0.0', port=5001)
