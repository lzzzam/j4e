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
    jobs = [{"title" : "Job#1", "company" : "company#1", "place" : "place#1"},
            {"title" : "Job#2", "company" : "company#2", "place" : "place#2"},
            {"title" : "Job#3", "company" : "company#3", "place" : "place#3"},
            {"title" : "Job#2", "company" : "company#2", "place" : "place#2"},
            {"title" : "Job#2", "company" : "company#2", "place" : "place#2"},
            {"title" : "Job#2", "company" : "company#2", "place" : "place#2"},
            {"title" : "Job#2", "company" : "company#2", "place" : "place#2"},
            {"title" : "Job#2", "company" : "company#2", "place" : "place#2"},
            {"title" : "Job#2", "company" : "company#2", "place" : "place#2"}]

    context = {"jobs" : jobs}
    return render_template('index.html.j2', context=context)


@app.route('/form', methods=('GET', 'POST'))
def form():
    #print(request.form['email'])
    return redirect('/')

with app.test_request_context():
    print(url_for('index'))
