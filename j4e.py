import os
import db
from flask import Flask
from flask import Blueprint, request, flash, g, redirect, render_template, request, session, url_for, make_response

jobs = [{"title" : "Job#1", "company" : "company#1", "place" : "place#1"},
        {"title" : "Job#2", "company" : "company#2", "place" : "place#2"},
        {"title" : "Job#3", "company" : "company#3", "place" : "place#3"},
        {"title" : "Job#2", "company" : "company#2", "place" : "place#2"},
        {"title" : "Job#2", "company" : "company#2", "place" : "place#2"},
        {"title" : "Job#2", "company" : "company#2", "place" : "place#2"},
        {"title" : "Job#2", "company" : "company#2", "place" : "place#2"},
        {"title" : "Job#2", "company" : "company#2", "place" : "place#2"},
        {"title" : "Job#2", "company" : "company#2", "place" : "place#2"}]

# create and configure the app
app = Flask(__name__)
app.config.from_mapping(
    DATABASE=os.path.join(app.instance_path, "jobs.sqlite"),
)

db.init_app(app)

@app.route('/')
def index():
    if (request.cookies.get('subscribed-to-newsletter') == "1") | (request.cookies.get('hidden-subscribe-box') == "1"):
        showEmailBox = False
    else:
        showEmailBox = True
        
    context = {"jobs" : jobs, "showEmailBox" : showEmailBox}
    return render_template('index.html.j2', context=context)


@app.route('/form', methods=('GET', 'POST'))
def form():
    print(request.form['email'])
    resp = make_response('', 204)
    resp.set_cookie(key='subscribed-to-newsletter', value = "1")
    return resp

@app.route('/close_form')
def close_form():
    print('close form')
    resp = make_response('', 204)
    resp.set_cookie(key='hidden-subscribe-box', value = "1", max_age=60)
    return resp
    

with app.test_request_context():
    print(url_for('index'))
