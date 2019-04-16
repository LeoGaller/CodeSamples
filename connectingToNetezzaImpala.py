# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 16:15:34 2019

@author: Leonardo.Galler
@note: Conectar no netezza
"""
import pyodbc
# Visualizing the available data sources
#print(pyodbc.dataSources())

conn = pyodbc.connect("DRIVER={NetezzaSQL}; SERVER= *** ; PORT=5480;DATABASE= *** ; UID=  USER ; PWD= *** ;")

# Define Cursor
cursor = conn.cursor()

# Execute SQL statement and store result in cursor
cursor.execute("SELECT * FROM table;")

# Display the content of cursor
while True:
    row=cursor.fetchone()
    if not row:
        break
    print(row)

# conda install -c anaconda impyla    
from impala.dbapi import connect
conn = connect(host='impala-host-name', port=21050)
cursor = conn.cursor()
cursor.execute('select * from table ')
print (cursor.description ) # prints the result set's schema
results = cursor.fetchall()