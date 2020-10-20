import flask 
import json 
import os
from flask_pymongo import PyMongo
from flask import request, jsonify
from flask_cors import CORS, cross_origin
from flask import render_template
import creds

class Stack:
    def _data_validate(self):
        self._stack['size']=len(self._stack['data'])

    def __init__(self,elements=[], filename="nil" ):
        self._stack={}
        self._stack['size']=[]
        self._stack['data']=elements
        self._stack['size']=len(elements)
    
    def pop(self):
        if not self._stack['size']:
            raise Exception("stack Exausted")
        temp=self._stack['data'][self._stack['size']-1]
        del self._stack['data'][self._stack['size']-1]
        self._stack['size']=len(self._stack['data'])
        
        return temp

    def empty_stack(self):
        self._stack["data"]=[]
        self._data_validate()

    def push(self,newElement=""):
        self._stack['data'].append(newElement)
        self._stack['size']=len(self._stack['data'])
        return 0

    def is_empty(self):
        if self._stack['size']:
            return 0
        else:
            return 1 
    
    def size(self):
            temp=self._stack['size']
            return temp
    
    def top(self):
        if not self._stack['size']:
            raise Exception("stack empty")
        return self._stack['data'][self._stack['size']-1]

    def stack(self):
        temp=self._stack['data']
        return temp 

    def raw_stack(self):
        temp=self._stack
        return temp


#  APP CONFIG 
app = flask.Flask(__name__)
CORS(app, support_credentials=True)
app.config["DEBUG"] = False

app.config['MONGO_URI'] = creds.MONGO_DB_URI
mongo = PyMongo(app)
stackdb=mongo.db.stack.find({"name" :"stack0"})[0]
stack = Stack(elements=stackdb['data'])


@app.route("/")
def index():
    return render_template("index.html")

@app.route('/stack',methods=['GET'])
def view_stack():
    # response=flask.Response()
    # response.status_code=200
    # response.status="OK"
    # print(stack.raw_stack())
    # response.response=json.dumps(stack.raw_stack())
    # response.headers["Access-Control-Allow-Origin"] = "*"
    # response.data="json"
    # response.headers["Content-Type"]="application/json"
    return json.dumps(stack.raw_stack()),200

@app.route('/pop',methods=['GET'])
def pop():
    stack.pop()
    return "POP OK",200

@app.route('/filesave',methods=['GET'])
def fileupdate():
    # stack.fileupdate()
    temp={
        "$set":{
        "data":stack.stack(),
        "size":stack.size()
        }
    }
    # temp['$data']=[]
    # temp['$size']=stack.size()
    # temp['$data']=stack.stack()
    mongo.db.stack.update_one({"name":"stack0"},temp)
    return "fileupdate OK",200

@app.route('/push',methods=['POST','OPTIONS'])
def push():
    stack.push(request.args['data'])
    return "PUSH OK",200
    
@app.route('/remake',methods=['GET'])
def remake():
    # stack.sync_file()
    stackdb=mongo.db.stack.find({"name" :"stack0"})[0]

    stack._stack['data'] = stackdb['data']
    stack._data_validate()
    return "OK",200


if __name__ == "__main__":
    app.run()