
from flask import Flask,request

# https://pypi.python.org/pypi/Flask-Cors
from flask_cors import CORS, cross_origin

# https://pythonspot.com/mysql-with-python/
import mysql.connector 
import json
import datetime

#def myconverter(o):
#    if isinstance(o, datetime.datetime):
#        return o.__str__()
#    else:
#        return json.JSONEncoder.default(self, o)


class JSONDataTypesEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            #return obj.isoformat()
            return obj.__str__()
        if isinstance(obj, bytearray):
            return obj.decode('utf-8').__str__()
            ##str(obj)
        else:
            return json.JSONEncoder.default(self, obj)


app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}}, methods=['GET'])


@app.route("/api/v1/etl_job_start_end",methods=['GET'])
def getLagData():

#  conn = mysql.connector.connect(user='python', password='Python123$', host='127.0.0.1', database='python')
    conn = mysql.connector.connect(user='python', password='Python123$',
                              host='127.0.0.1',
                              database='titan')

    cursor = conn.cursor()
    cursor.execute('SELECT etl_process_id, etl_process_start_time, IFNULL(etl_process_end_time, NOW()) AS etl_process_end_time, etl_process_name etl_process_name, etl_process_status \
        FROM titan.v_etl_load_runs WHERE etl_process_start_time BETWEEN DATE_SUB(NOW(), INTERVAL 300 HOUR) AND NOW()');

    rows = cursor.fetchall()
    row_headers=[x[0] for x in cursor.description] #this will extract row headers

    json_data=[]
    for result in rows:
        json_data.append(dict(zip(row_headers,result)))
    #return json.dumps(json_data, default = myconverter)
    return json.dumps(json_data, cls=JSONDataTypesEncoder)
    ##return json.dumps(json_data);
    ##return json_data

app.run(port=5010, debug = True)