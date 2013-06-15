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

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')
