import os
from db import init_app, get_db, close_db, query_db
from flask import Flask
from flask import Blueprint, request, flash, g, redirect, render_template, request, session, url_for, make_response

# create and configure the app
app = Flask(__name__)
init_app(app)

@app.route('/', methods=('GET', 'POST'))
def index():
    return render_template('landing-page.html.j2')

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0')