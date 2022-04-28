from flask import Flask, render_template, request,jsonify
#from models import *
# from pyforms import SearchForm
from flaskext.mysql import MySQL
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
app.config['MYSQL_DATABASE_USER'] = 'jrd179'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Xzu39641'
app.config['MYSQL_DATABASE_DB'] = 'covid_tracker_DB'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql = MySQL()
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()

app.secret_key = "Utn34dfRgfdi23"
app.config['SESSION_COOKIE_NAME'] = 'User Cookie'


@app.route("/", methods=["POST", "GET"])
def index():
    return render_template("index.html")

def res_search():
    searchbox = request.form.get("text")
    cursor = mysql.connection.cursor()
    query = "SELECT s.sid FROM STUDENT s, STUDENT s2, TESTS t WHERE t.sid = s.sid AND t.has_covid = 1 AND s2.sid = {}% AND s2.address = s.address".format(searchbox)#This is just example query , you should replace field names with yours
    cursor.execute(query)
    result = cursor.fetchall()
    #result = searchbox
    test = "testing that this page works?"
    return jsonify(result, test)

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        user_input = request.form['text']

        #perform database search using input
        cursor.execute("SELECT s.sid FROM STUDENT s, STUDENT s2, RESIDENCE r, LIVESIN l, TESTS t WHERE s.sid = l.sid AND r.address = l.address AND t.sid = s.sid AND s2.sid = (%s) s2.address = r.address",(user_input))
        conn.commit()
        data = cursor.fetchall()

        # all in the search box will return all the tuples
        if len(data) == 0:
            no_such_id = "No such ID exists in our records"
            return render_template('search.html', data=no_such_id)
        return render_template('search.html', data=data)
    return render_template('search.html')


@app.route("/livesearch",methods=["POST","GET"])
def livesearch():
    searchbox = request.form.get("text")
    cursor = mysql.connection.cursor()
    query = "SELECT s.sid FROM STUDENT s, STUDENT s2, TESTS t WHERE t.sid = s.sid AND t.has_covid = 1 AND s2.sid = {}% AND s2.address = s.address".format(searchbox)
    cursor.execute(query)
    result = cursor.fetchall()
    #result = searchbox
    test = "testing that this page works?"
    return jsonify(result, test)


#three search functions:
# given a user types their student id, return all people who have tested positive who live in the same residence hall
#                                    , return all people who have tested positive who are in the same classes as them
#                                    , return all people who have tested positive who are in the same organizations as them
# return a count of all people who have covid on campus
    

def residence_search(userInput):
    # given a user input of their student id, return the number of people in their residence hall that have covid
    # this is done to preserve anonymity for those with covid

    query = ''

    return query


if __name__ == '__main__':
    app.run(port=5000, debug=True)