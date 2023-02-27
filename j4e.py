import os
from db import init_app, get_db, close_db, query_db
from flask import Flask
from flask import Blueprint, request, flash, g, redirect, render_template, request, session, url_for, make_response

# create and configure the app
app = Flask(__name__)
app.config.from_mapping(
    DATABASE="jobs.sql",
)

init_app(app)

@app.before_request
def readCookies():
    if (request.cookies.get('subscribed-to-newsletter') == "1") | \
       (request.cookies.get('hidden-subscribe-box') == "1"):
        g.showEmailBox = False
    else:
        g.showEmailBox = True
    
    g.search_text = request.cookies.get('search-text', "")
    g.page_offset = int(request.cookies.get('page-offset', "0"))

@app.after_request
def updateCookies(response):
    response.set_cookie(key='page-offset', value = str(g.page_offset), max_age=60)
    response.set_cookie(key='search-text', value = g.search_text, max_age=60)
    return response

@app.route('/')
def index():        
    g.search_text = request.args.get("search-text", "")
    g.search_country = request.args.get("search-country", "")
    jobs = query_db(f"select * from jobs where  (title like '%{g.search_text}%' or \
                                                company like '%{g.search_text}%' or \
                                                description like '%{g.search_text}%') \
                                            and (country like '%{g.search_country}%') \
                    limit 10")
    if len(jobs) > 0:
        context = {"jobs" : jobs, "showEmailBox" : g.showEmailBox, "noResult": False}    
        resp = make_response(render_template('index.html.j2', context=context))
    else:
        context = {"jobs" : jobs, "showEmailBox" : g.showEmailBox, "noResult": True}    
        resp = make_response(render_template('index.html.j2', context=context))

    return resp


@app.route('/nextjobs')
def getJobs():
    g.page_offset = g.page_offset + 10 
    jobs = query_db(f"select * from jobs where  title like '%{g.search_text}%' or \
                                                company like '%{g.search_text}%' or \
                                                description like '%{g.search_text}%' \
                    limit 10 offset {g.page_offset}")
    
    if len(jobs) != 0:
        context = {"jobs" : jobs}
        resp = make_response(render_template('jobs.html.j2', context=context))
    else:
        resp = make_response('', 204)
        
    return resp


@app.route('/form', methods=('GET', 'POST'))
def form():
    resp = make_response('', 204)
    # never show email box again
    resp.set_cookie(key='subscribed-to-newsletter', value = "1")
    return resp

@app.route('/cookies', methods=('GET','POST'))
def close_form():
    # set cookies from json data
    if request.method == 'POST':
        data = request.json
        if data.get('hidden_subscribe_box'):
            resp = make_response('', 204)
            resp.set_cookie(key='hidden-subscribe-box', value = "1", max_age=60)
    else:
        resp = make_response('', 400)
        
    return resp
