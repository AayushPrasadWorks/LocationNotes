import pymongo
from flask import Flask
from flask import request
from flask import render_template
from server import server
from time import gmtime, strftime
from datetime import date

app = Flask(__name__)

myclient = pymongo.MongoClient('127.0.0.1', 27017)

@app.route('/', methods=['GET'])
def forms():
    print(request.data)
    if request.method == 'GET':
        name = request.form['Title']
        ser = server()
        ser.getPersonMessage(name,myclient)
    return 'OK'

@app.route('/', methods=['POST'])
def form_insert():
    print(request.data)
    if request.method == 'POST':
       name = request.form['Title']
       message = request.form['Notes']
       today = date.today()
       ser = server()
       ser.add(name, message,today.isoformat(),myclient)
    return 'OK'

@app.route('/', methods=['PUT'])
def form_update():
    print(request.data)
    if request.method == 'PUT':
       name = request.form['Title']
       new_message = request.form['Notes']
       today = date.today()
       ser = server()
       ser.update(name,new_message,today.isoformat(),myclient)
    return 'Success'

@app.route('/', methods=['DELETE'])
def form_delete():
    print(request.data)
    if request.method == 'DELETE':
        name = request.form['Title']
        ser = server()
        ser.delete(name,myclient)
    return 'OK'


if __name__ == "__main__":
    app.run()
