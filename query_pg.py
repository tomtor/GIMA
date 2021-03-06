#!/usr/bin/python3
# -*- coding: utf-8 -*-

import psycopg2
import sys


con = None

try:
    con = psycopg2.connect(database='gima', user='tom') 
    cur = con.cursor()
    cur.execute('SELECT version()')          
    ver = cur.fetchone()
    print(ver)

    while True:
        q = input("\nEnter query: ")
        cur.execute("SELECT * FROM documenten where to_tsvector('dutch', doc) @@ to_tsquery('dutch', '" + q + "')")
        rows= cur.fetchall()
        for doc in rows:
            print(doc)
    
except psycopg2.DatabaseError as e:
    print('Error %s' % e)
    sys.exit(1)
    
finally:
    
    if con:
        con.close()
