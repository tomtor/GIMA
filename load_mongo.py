#!/usr/bin/python3
# -*- coding: utf-8 -*-

# This is a Python 3 script!

from pymongo import MongoClient
import sys


client = MongoClient()

try:
     
    db = client.gima
    coll = db.geboorte  
    
    coll.drop()

    count = 0
    doc = ''
    f = open('data/geboorte.txt', 'r')
    for line in f:
        if len(line) == 1:
            count = count + 1
            print(count)
            for i in range(0, 1000):
                coll.insert({"tekst": doc, "bron": "demo"})
            doc = ''
        else:
            doc = doc + line
    f.close()

    print("Build index...")
    #db.geboorte.ensureIndex({"tekst": "text"}, {"default_language": "dutch"})

except:
    print('Error:', sys.exc_info()[0])
    sys.exit(1)
    
    
finally:
    
    if client:
        client.disconnect()
