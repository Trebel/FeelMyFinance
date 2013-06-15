from flask import render_template, flash, redirect, request, json
from app import app
from forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Kelly' }
    return render_template('index.html',
        title = 'Home',
        user = user
        )

@app.route('/chart')
def chart():
    user = { 'nickname': 'Kelly' }
    return render_template('chart.html',
        title = 'chart',
        user = user
        )

@app.route('/personality', methods = ['POST'])
def personality():
    if request.headers['Content-Type'] == 'text/plain':
        return request.data
    elif request.headers['Content-Type'] == 'application/json':
        return "JSON Message: " + json.dumps(request.json)
    elif request.headers['Content-Type'] == 'application/octet-stream':
        f = open('./binary', 'wb')
        f.write(request.data)
        f.close()
        return "Binary message written!"
    else:
        return "415 Unsupported Media Type"
