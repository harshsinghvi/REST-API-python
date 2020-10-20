import flask
import json
from flask import request, jsonify
from flask_cors import CORS, cross_origin
from flask_pymongo import PyMongo
from datetime import datetime

## importing credentials for mongo db database refer sample.creds.py to make a creds.py module for your credentials
import creds

#  APP CONFIG 
app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config['MONGO_URI'] = creds.MONGO_DB_URI

mongo = PyMongo(app)
CORS(app, support_credentials=True)


# API resourses
@app.route('/', methods=['GET'])
def home():
    return "<h1>Doccumentation</h1><p>This site is a prototype API for online assisment and forms collection.</p>"

@app.route('/db', methods=['GET'])
def db_test():
    que=mongo.db.questions.find()
    dict=[]
    for i in que:
        temp={
            'id':i['id'],
            'que':i['que'],
            'choices':i['choices']
        }
        dict.append(temp)
    return jsonify(dict)

@app.route('/db-in', methods=['POST'])
def db_test_in():
    que=mongo.db.responses
    temp=request.get_json()
    temp['timestamp']=str(datetime.now())
    if que.insert_one(temp).acknowledged:
        return "OK",200
    return "ERROR",404

@app.route('/db-out',methods=['GET'])
def db_out():
    dbResponses=mongo.db.responses.find()
    dict=[]
    for i in dbResponses:
        temp={
            'id':str(i['_id']),
            'name':i['name'],
            'email':i['email'],
            'timestamp':i['timestamp'],
            'responses':i['responses']
        }
        dict.append(temp)
    return jsonify(dict)

@app.route('/questions',methods=['GET'])
@cross_origin(supports_credentials=True)
def send_questions():
    file=open('./data/questions.json')
    temp=file.read()
    file.close()
    response = flask.Response()
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Content-Type"]="application/json"
    response.response=temp
    return response


@app.route('/note_response',methods=['POST'])
def note_responses():
    response={}
    response['responses']={}
    if request.is_json:
        f=open("./data/responses.json")
        temp=json.loads(f.read())
        temp1=request.get_json()
        print(temp1)
        temp.append(temp1)
        f.close()
        f=open("./data/responses.json",'w')
        f.write(json.dumps(temp))
        f.close()
        db_test_in(request,True)
        return "OK",200
    else: 
        return "Please send data with desired format",400

@app.route('/get-responses',methods=['GET'])
def responses():
    file = open('./data/responses.json')
    temp=file.read()
    file.close()
    response = flask.Response()
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Content-Type"]="application/json"
    response.response=temp
    return response

@app.route('/get-result',methods=['GET'])
def result():
    return "Under construction wait "

def db_test_in(request,out):
    if not out:
        return 1
    que=mongo.db.app
    que.insert_one(request.get_json())
    print(request.get_json())
    return 0

if __name__ == "__main__":
    app.run()