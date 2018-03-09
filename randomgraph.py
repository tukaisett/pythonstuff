#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 21:02:15 2018

@author: tukai
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 11:30:19 2018

@author: tukai
"""

import plotly.plotly as py
import plotly
import plotly.graph_objs as go
import MySQLdb
import random

 
#py.tools.set_credentials_file(username='arindamsett_mw', api_key='tSNgiVXCus0253Pjor0x')

# Add data
month = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
         'August', 'September', 'October', 'November', 'December']
high_2000 = [32.5, 37.6, 49.9, 53.0, 69.1, 75.4, 76.5, 76.6, 70.7, 60.6, 45.1, 29.3]
low_2000 = [13.8, 22.3, 32.5, 37.2, 49.9, 56.1, 57.7, 58.3, 51.2, 42.8, 31.6, 15.9]
high_2007 = [36.5, 26.6, 43.6, 52.3, 71.5, 81.4, 80.5, 82.2, 76.0, 67.3, 46.1, 35.0]
low_2007 = [23.6, 14.0, 27.0, 36.8, 47.6, 57.7, 58.9, 61.2, 53.3, 48.5, 31.0, 23.6]
high_2014 = [28.8, 28.5, 37.0, 56.8, 69.7, 79.7, 78.5, 77.8, 74.1, 62.6, 45.3, 39.9]
low_2014 = [12.7, 14.3, 18.6, 35.5, 49.9, 58.0, 60.0, 58.6, 51.7, 45.2, 32.2, 29.1]



#db = MySQLdb.connect(host="awsmysql.ckacjaidpun5.us-west-1.rds.amazonaws.com",  # your host 
#                    user="root",       # username
#                    passwd="geewhiz911",     # password
 #                   db="python")   # name of the database

db = MySQLdb.connect(host="localhost",  # your host 
                   user="root",       # username
                   passwd="geewhiz911",     # password
                     db="python")   # name of the database

# Create a Cursor object to execute queries.
cur = db.cursor()
 
# Select data from table using SQL query.
#cur.execute("truncate table test_table")

# Build the x/y axis data
x_axis = list()
y_axis = list()

graph_range = 100 

for x in range(graph_range):
    x_axis.append(x)
    y_axis.append(random.randint(80,100))


cur.execute("truncate table test_table")

for x in range(graph_range):
    cur.execute("insert into test_table(column1, column2) VALUES(%s,%s)",(x, y_axis[x]))
    

cur.execute("commit")    

# Create and style traces
trace0 = go.Scatter(
    x = x_axis,
    y = y_axis,
    name = 'Angular Random Graph',
    line = dict(
        color = ('rgb(205, 12, 24)'),
        width = 4)
   # ,       shape = 'spline')
)

trace01 = go.Scatter(
    x = x_axis,
    y = y_axis,
    name = 'Smooth Random Graph',
    line = dict(
        color = ('rgb(120, 100, 156)'),
        width = 4,
        shape = 'spline')
)
   
    
trace1 = go.Scatter(
    x = month,
    y = low_2014,
    name = 'Low 2014',
    line = dict(
        color = ('rgb(22, 96, 167)'),
        width = 4)
)
trace2 = go.Scatter(
    x = month,
    y = high_2007,
    name = 'High 2007',
    line = dict(
        color = ('rgb(205, 12, 24)'),
        width = 4,
        dash = 'dash') # dash options include 'dash', 'dot', and 'dashdot'
)
trace3 = go.Scatter(
    x = month,
    y = low_2007,
    name = 'Low 2007',
    line = dict(
        color = ('rgb(22, 96, 167)'),
        width = 4,
        dash = 'dash')
)
trace4 = go.Scatter(
    x = month,
    y = high_2000,
    name = 'High 2000',
    line = dict(
        color = ('rgb(205, 12, 24)'),
        width = 4,
        dash = 'dot')
)
trace5 = go.Scatter(
    x = month,
    y = low_2000,
    name = 'Low 2000',
    line = dict(
        color = ('rgb(22, 96, 167)'),
        width = 4,
        dash = 'dot')
)
#data = [trace0, trace1, trace2, trace3, trace4, trace5]

data = [trace0, trace01]

# Edit the layout
layout = dict(title = 'Average High and Low Temperatures in New York',
              xaxis = dict(title = 'Month'),
              yaxis = dict(title = 'Temperature (degrees F)'),
              )

fig = dict(data=data, layout=layout)
py.plot(fig, filename='styled-line')


plotly.offline.plot(fig, filename='styled-line')

