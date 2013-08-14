#!/usr/bin/python3
# -*- coding: utf-8 -*-

# This is a Python 3 script!

from pymongo import MongoClient
import sys


client = MongoClient()

try:
     
    db = client.gima 
    coll = db.geboorte

    while True:
        q = input("\nEnter query: ")
        results = db.command('text', 'geboorte', search=q)
        print(str(results['results']))
    
except:
    print('Error:', sys.exc_info()[0])
    sys.exit(1)
    
    
finally:
    
    if client:
        client.disconnect()
