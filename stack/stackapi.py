import flask 
import json 
import stack 

from flask import request, jsonify
from flask_cors import CORS, cross_origin

#  APP CONFIG 
app = flask.Flask(__name__)
CORS(app, support_credentials=True)
app.config["DEBUG"] = True

stack = stack.Stack(filename="file.json")


@app.route('/',methods=['GET'])
def view_main():
    response=flask.Response()
    response.status_code=200
    response.status="OK"
    response.response=json.dumps(stack.raw_stack())
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Content-Type"]="application/json"
    return response

@app.route('/pop',methods=['GET'])
def pop():
    stack.pop()
    return "POP OK",200

@app.route('/filesave',methods=['GET'])
def fileupdate():
    stack.fileupdate()
    return "fileupdate OK",200

@app.route('/push',methods=['POST','OPTIONS'])
def push():
    stack.push(request.args['data'])
    return "PUSH OK",200
    
@app.route('/remake',methods=['GET'])
def remake():
    stack.sync_file()
    return "OK"


if __name__ == "__main__":
    app.run()