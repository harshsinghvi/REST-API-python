from flask import request, jsonify,  Flask, session, redirect, url_for, escape, render_template
# from flask_cors import CORS, cross_origin
# from flask_pymongo import PyMongo,ObjectId

app = Flask(__name__)
app.secret_key = 'Superrandom'

session_details = ['username', 'password']

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login', methods = ['GET', 'POST'])
def login():
   if request.method == 'POST':
        session['username'] = request.form['username']
        session['password'] = request.form['password']
        return "Login"+str(session['username']),200
   return render_template("login.html")

@app.route('/logout')
def logout():
    # remove the username from the session if it is there
    # session.pop('username', None)
    for d in session_details: 
        session.pop(d, None)
    return redirect(url_for('index'))

@app.route('/test-auth',methods=['GET','POST'])
def auth():
    if session['username']=='harsh':
        return "HS",200
    return "OK",200

@app.route('/test-login/<username>',methods=['GET','POST'])
def lo(username):
    session['username'] = username
    return username,200

@app.route('/test-connection',methods=['GET','POST'])
def func():
    return "OK",200

if __name__ == "__main__":
    app.run(host="0.0.0.0")