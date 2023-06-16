from flask import Flask, request
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'Superrandom'

@app.route('/test-connection',methods=['GET','POST'])
def func():
    return "OK",200

@app.route('/test-file',methods=['GET','POST'])
def file():
    a = request.files['media']
    # a.save('test.jpg')


    print(a)
    a.save('./data/'+str(datetime.now())+"-" +  a.filename)

    # f = open("test.jpg", 'wb')
    # f.write(a.read())
    # f.close()
    a.close()
    return "OK",200




if __name__ == "__main__":
    app.run(host="0.0.0.0")