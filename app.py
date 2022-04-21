from flask import Flask, render_template, request,jsonify
#from models import *
# from pyforms import SearchForm
import os


app = Flask(__name__)
# database connection via integrated db in elastic beanstalk
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
    }

app.secret_key = "Utn34dfRgfdi23"
app.config['SESSION_COOKIE_NAME'] = 'User Cookie'


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/livesearch",methods=["POST","GET"])
def livesearch():
    searchbox = request.form.get("text")
    #cursor = mysql.connection.cursor()
    query = "select word_eng from words where word_eng LIKE '{}%' order by word_eng".format(searchbox)#This is just example query , you should replace field names with yours
    #cursor.execute(query)
    #result = cursor.fetchall()
    result = searchbox
    test = "testing that this page works?"
    return jsonify(result, test)

    

def residence_search(userInput):
    # given a user input of their student id, return the number of people in their residence hall that have covid
    # this is done to preserve anonymity for those with covid

    query = ''

    return query


if __name__ == '__main__':
    app.run(port=5000, debug=True)