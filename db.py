import sqlite3

import click
from flask import current_app, g
import requests
import pydenticon

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect("jobs.sql" )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
        
def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def create_job(conn, job):
    """
    Create a new job into the job table
    :param conn:
    :param project:
    :return: project id
    """
    country = job['country']
    place = job['place']
    date = job['date']
    title = job['title']
    company = job['company']
    description = job['description']
    logo = job['company']+".png"
    link= job['link']
    jobData = (country, place, date, title, company, description, logo, link)
    
    sql = ''' INSERT INTO jobs(country,place,date,title,company,description,logo,link)
            VALUES(?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, jobData)
    conn.commit()
    return cur.lastrowid

def get_random_data_from_mockaroo():
    # sending get request and saving the response as response object
    r = requests.get(url = "https://my.api.mockaroo.com/jobcard.json?key=bed7e440")
    
    # extracting data in json format
    return r.json()

def generate_logo(company):
    # Set-up a list of foreground colours (taken from Sigil).
    foreground = [ "rgb(45,79,255)",
                "rgb(254,180,44)",
                "rgb(226,121,234)",
                "rgb(30,179,253)",
                "rgb(232,77,65)",
                "rgb(49,203,115)",
                "rgb(141,69,170)" ]
    generator = pydenticon.Generator(5, 5, foreground=foreground)
    # Set-up the padding (top, bottom, left, right) in pixels.
    padding = (20, 20, 20, 20)

    # Generate a 200x200 identicon with padding around it, and invert the
    # background/foreground colours.
    identicon = generator.generate(company, 60, 60, padding=padding, inverted=True)
    

    # Identicon can be easily saved to a file.
    f = open("./static/images/logos/" + company + ".png", "wb")
    f.write(identicon)
    f.close()

def fill_db(conn, data):
    for job in data:
        create_job(conn, job)


def create_mock_db():
    db = create_connection("jobs.sql")

    with open('schema.sql') as f:
        db.executescript(f.read())
        
    data = get_random_data_from_mockaroo()
    fill_db(db, data)
    for job in data:
        generate_logo(job['company'])
