#!/usr/bin/python
# -*- coding: utf-8 -*-

from pymongo import MongoClient
import sys


client = MongoClient()

try:
     
    db = client.gima 
    coll = db.geboorte

    while True:
        q = raw_input("\nEnter query: ")
        ### work in progress, continue from this point
        rows= cur.fetchall()
        for doc in rows:
            print doc
    
except psycopg2.DatabaseError, e:
    print 'Error %s' % e    
    sys.exit(1)
    
    
finally:
    
    if con:
        con.close()
