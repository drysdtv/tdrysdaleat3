from flask import Flask, render_template, redirect, url_for, request
import json
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import wtforms

app = Flask('app')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/robots')
def robots():
    return render_template('robots.html')


app.run(host='0.0.0.0', port=8080, debug=True)
