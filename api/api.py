import flask
from flask import request, jsonify
import sqlite3
import requests
import os
import flask_monitoringdashboard as dashboard



app = flask.Flask(__name__)
app.config["DEBUG"] = True
dashboard.bind(app)


@app.route('/dev',methods=['GET','POST','HS'])
def hs():
    if 'id' not in request.args:
        return "ERROR:ID NOT PASSED",400
    os.system('date >> log.txt')
    msg = "Hello "+ request.args['id']
    cmd = "echo " + msg + ">> log.txt"
    os.system(cmd)
    return "<h1> " + msg + "!!!</h1>"


@app.route('/echo/<message>',methods=['GET','POST','HS'])
def url_echo(message):
    return message
@app.route('/ip',methods=['GET','POST','HS'])
def relay_api():
    URL = "http://ip-api.com/json/"+request.args['ip']
    r = requests.get(url = URL) 
    return r.json()


@app.route('/web',methods=['GET','POST'])
def index():
    f=open("index.html")
    return f.read()

@app.route('/db',methods=['GET','POST'])
def db_view():
    if 'sql' not in request.args:
        return "ERROR:sql NOT PASSED",400
    
    sqliteConnection = sqlite3.connect('test.db')
    cursor = sqliteConnection.cursor()

    # sqlite_select_Query = request.args['sql']
    sqlite_select_Query ="SELECT * from people"
    cursor.execute(sqlite_select_Query)
    record = cursor.fetchall()
    cursor.close()
    print(type(record))
    msg = "SQLite Database Version is: " + str(record) + "<br>"
    for i in record:
        msg += str(i[0]) + "    " + i[1] + "    " +  str(i[2]) + "<br>"
    msg += "<br>"
    return msg

@app.errorhandler(404)
def page_not_found(e):
    return "<h1><strong>FUCK OFF !!!</strong></h1>", 404


app.run(host="0.0.0.0",port=80)
# app.run()
