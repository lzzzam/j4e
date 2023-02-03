import os
import db
from flask import Flask
from flask import Blueprint, request, flash, g, redirect, render_template, request, session, url_for


# create and configure the app
app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY="dev",
    DATABASE=os.path.join(app.instance_path, "jobs.sqlite"),
)

db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home/')
def homepage():
    return render_template('home/home.html')

@app.route('/form', methods=('GET', 'POST'))
def form():
    print(request.form['email'])
    return redirect('/')

with app.test_request_context():
    print(url_for('index'))
    print(url_for('homepage'))