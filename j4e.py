import os
from db import init_app, get_db, close_db, query_db
from flask import Flask
from flask import Blueprint, request, flash, g, redirect, render_template, request, session, url_for, make_response

flags = {
    "Austria"       :	"🇦🇹",
    "Belgium"	    :   "🇧🇪",
    "Czechia"	    :   "🇨🇿",
    "Denmark"	    :   "🇩🇰",
    "Finland"	    :   "🇫🇮",
    "France"	    :   "🇫🇷",
    "Germany"	    :   "🇩🇪",
    "Greece"	    :   "🇬🇷",
    "Hungary"	    :   "🇭🇺",
    "Ireland"	    :   "🇮🇪",
    "Italy"	        :   "🇮🇹",
    "Luxembourg"    :	"🇱🇺",
    "Netherlands"   :	"🇳🇱",
    "Norway"        :   "🇳🇴",
    "Poland"	    :   "🇵🇱",
    "Portugal"	    :   "🇵🇹",
    "Romania"	    :   "🇷🇴",
    "Spain"	        :   "🇪🇸",
    "Sweden"	    :   "🇸🇪",
    "Ukraine"       :   "🇺🇦"
}

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

@app.after_request
def updateCookies(response):
    return response

@app.route('/', methods=('GET', 'POST'))
def index():
    jobs = query_db(f"select * from jobs limit 10")     
    context = {"jobs" : jobs, "flags" : flags, "showEmailBox" : g.showEmailBox}
    resp = make_response(render_template('index.html.j2', context=context))
    return resp


@app.route('/search')
def search():
    g.search_text = request.args.get('text', "")
    g.search_country = request.args.get("country", "").lower()
    g.page_offset = int(request.args.get('offset', "0"))

    if g.search_country == "europe":
        g.search_country = ""

    sql_query = f"SELECT * FROM jobs WHERE  (title like '%{g.search_text}%' OR \
                                            company like '%{g.search_text}%' OR \
                                            description like '%{g.search_text}%' OR \
                                            place like '%{g.search_text}%') AND \
                                            country like '%{g.search_country}%'"

    jobs = query_db(sql_query + f"LIMIT 20 OFFSET {g.page_offset}")
    
    if len(jobs) > 0:
        if g.page_offset == 0:
            search_num = len(query_db(sql_query))
            context = {"jobs" : jobs, "flags" : flags, "search_num" : search_num}
        else:
            context = {"jobs" : jobs, "flags" : flags}
            
        return make_response(render_template('jobs.html.j2', context=context))

    if g.page_offset == 0:
        return make_response(render_template('nojobs.html.j2'))
    else:
        return '', 204

@app.route('/post', methods=('GET', 'POST'))
def post():
    resp = make_response(render_template('post.html.j2'), 200)
    return resp
    
@app.route('/form', methods=('GET', 'POST'))
def form():
    resp = make_response('', 204)
    # never show email box again
    resp.set_cookie(key='subscribed-to-newsletter', value = "1")
    return resp

@app.route('/cookies', methods=('GET','POST'))
def cookies():
    # set cookies from json data
    if request.method == 'POST':
        data = request.json
        if data.get('hidden_subscribe_box'):
            resp = make_response('', 204)
            resp.set_cookie(key='hidden-subscribe-box', value = "1", max_age=60)
    else:
        resp = make_response('', 400)
        
    return resp

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0')