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

    cur.execute("DROP TABLE documenten")
    cur.execute("CREATE TABLE documenten(id INT PRIMARY KEY, lexemes tsvector, doc text, bron varchar(100))")
    #cur.execute("INSERT INTO documenten VALUES(0, to_tsvector('dutch', 'Voorbeeld tekst'), 'Voorbeeld tekst', 'demo')")

    id = 0
    doc = ''
    f = open('data/geboorte.txt', 'r')
    for line in f:
        if len(line) == 1:
            id = id + 1
	    doc = doc.translate(None, '"\'')
            print doc
            cur.execute("INSERT INTO documenten VALUES(" + str(id) \
                + ", to_tsvector('dutch', '" + doc + "'), '" + doc + "', 'demo')")
            doc = ''
        else:
            doc = doc + line
    f.close()
    
    con.commit()
    

except psycopg2.DatabaseError, e:
    print 'Error %s' % e    
    sys.exit(1)
    
    
finally:
    
    if con:
        con.close()
