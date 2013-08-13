#!/usr/bin/python
# -*- coding: utf-8 -*-

from pymongo import MongoClient
import sys


client = MongoClient()

try:
     
    db = client.gima
    coll = db.geboorte  
    
    coll.drop()

    id = 0
    doc = ''
    f = open('data/geboorte.txt', 'r')
    for line in f:
        if len(line) == 1:
            id = id + 1
            #doc = doc.translate(None, '"\'')
            print(id)
            coll.insert({"tekst": doc, "bron": "demo"})
            doc = ''
        else:
            doc = doc + line
    f.close()

except:
    print('Error:', sys.exc_info()[0])
    sys.exit(1)
    
    
finally:
    
    if client:
        client.disconnect()
    print('Maak handmatig nog een index met dit commando: db.geboorte.ensureIndex({tekst: "text"}, {default_language: "dutch"})')
