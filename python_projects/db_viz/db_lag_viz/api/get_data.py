# Prerequisites: Python 2.7, Flask 0.12.2, Python-Mysql connector
# sudo pip install Flask
# sudo apt install python-mysqldb
# sudo pip install -U flask-cors

# Run with:
# FLASK_APP=hello.py flask run

# http://flask.pocoo.org/docs/0.12/api/#flask.request
from flask import Flask,request

# https://pypi.python.org/pypi/Flask-Cors
from flask_cors import CORS, cross_origin

# https://pythonspot.com/mysql-with-python/
import mysql.connector 
import json
import datetime

def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}}, methods=['GET'])


@app.route("/api/v1/lag_times",methods=['GET'])
def getLagData():

#  conn = mysql.connector.connect(user='python', password='Python123$', host='127.0.0.1', database='python')
    conn = mysql.connector.connect(user='python', password='Python123$',
                              host='127.0.0.1',
                              database='python')

    cursor = conn.cursor()
    cursor.execute('select STR_TO_DATE(CONCAT(date_format(reading_date, \'%Y-%m-%d\'), \' \', reading_time), \'%Y-%m-%d %H:%i:%s\') reading_date_time, reading_lag_time FROM python.db02_lag_history WHERE reading_date BETWEEN DATE_SUB(DATE(NOW()), INTERVAL 30 DAY) AND DATE(NOW())');

    rows = cursor.fetchall()
    row_headers=[x[0] for x in cursor.description] #this will extract row headers

    json_data=[]
    for result in rows:
        json_data.append(dict(zip(row_headers,result)))
    return json.dumps(json_data, default = myconverter)


app.run()
