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

    cur = con.cursor()
  
    cur.execute("CREATE TABLE documenten(id INT PRIMARY KEY, lexemes tsvector, bron varchar(100))")
    cur.execute("INSERT INTO documenten VALUES(0, to_tsvector('Voorbeeld tekst'), 'demo')")
    
    con.commit()
    

except psycopg2.DatabaseError, e:
    print 'Error %s' % e    
    sys.exit(1)
    
    
finally:
    
    if con:
        con.close()
