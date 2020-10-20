import flask 
import json 
from  que import Que

from flask import request, jsonify
from flask_cors import CORS, cross_origin

#  APP CONFIG 
app = flask.Flask(__name__)
CORS(app, support_credentials=True)
app.config["DEBUG"] = True

que = Que(filename="file.json")


@app.route('/',methods=['GET'])
def view_main():
    response=flask.Response()
    response.status_code=200
    response.status="OK"
    response.response=json.dumps(que.raw_que())
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Content-Type"]="application/json"
    return response

@app.route('/get',methods=['GET'])
def pop():
    que.get()
    return "GET OK",200

@app.route('/filesave',methods=['GET'])
def fileupdate():
    que.fileupdate()
    return "fileupdate OK",200

@app.route('/put',methods=['POST','OPTIONS'])
def push():
    que.put(int(request.args['data']))
    return "PUSH OK",200

@app.route('/remake',methods=['GET'])
def remake():
    que.sync_file()
    return "OK",200

if __name__ == "__main__":
    app.run()