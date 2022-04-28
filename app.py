from flask import Flask, render_template, request,jsonify
#from models import *
# from pyforms import SearchForm
from flaskext.mysql import MySQL
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
# database connection via integrated db in elastic beanstalk
"""
if 'RDS_HOSTNAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'mysql',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    } """

# Database connection info. Note that this is not a secure connection.
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://jrd179:Xzu39641@localhost/covid_tracker_DB'
app.config['MYSQL_DATABASE_USER'] = 'jrd179'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Xzu39641'
app.config['MYSQL_DATABASE_DB'] = 'covid_tracker_DB'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql = MySQL()
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()

print(cursor)

app.secret_key = "Utn34dfRgfdi23"
app.config['SESSION_COOKIE_NAME'] = 'User Cookie'


@app.route("/", methods=["POST", "GET"])
def index():
    return render_template("index.html")


@app.route('/search', methods=['GET', 'POST'])
def search():
    user_input_home = request.args.get('searchterm')
    print(user_input_home)
    if request.method == "POST":
        user_input_home = request.form['text']


    #perform database search using input
    query = "SELECT DISTINCT (s.Sid) FROM STUDENTS s, STUDENTS s2, TESTS t WHERE t.Sid = s.Sid AND t.hascovid = 1 AND s2.Sid = '{}%' AND s2.Address = s.Address AND s2.Sid != s.Sid".format(user_input_home)
    cursor.execute(query)
    conn.commit()
    data = cursor.fetchall()

    # all in the search box will return all the tuples
    if len(data) == 0:
        no_such_id = "No such ID exists in our records"
        return render_template('search.html', data=no_such_id)
    return render_template('search.html', data=data)



if __name__ == '__main__':
    app.run(port=5000, debug=True)