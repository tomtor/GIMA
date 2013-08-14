#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import sys


con = None

try:
     
    con = psycopg2.connect(database='gima', user='tom') 
    cur = con.cursor()
    cur.execute('SELECT version()')          
    ver = cur.fetchone()
    print ver    

    while True:
        q = raw_input("\nEnter query: ")
        cur.execute("SELECT * FROM documenten where lexemes @@ to_tsquery('dutch', '" + q + "')")
        rows= cur.fetchall()
        for doc in rows:
            print doc
    
except psycopg2.DatabaseError, e:
    print 'Error %s' % e    
    sys.exit(1)
    
    
finally:
    
    if con:
        con.close()
