#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 22:42:12 2018

@author: tukai
"""

import MySQLdb
 
db = MySQLdb.connect(host="awsmysql.ckacjaidpun5.us-west-1.rds.amazonaws.com",  # your host 
                     user="root",       # username
                     passwd="geewhiz911",     # password
                     db="python")   # name of the database
 
# Create a Cursor object to execute queries.
cur = db.cursor()
 
# Select data from table using SQL query.
cur.execute("SELECT * FROM Employees")
 
# print the first and second columns      
for row in cur.fetchall() :
    print row[0], " ", row[1]