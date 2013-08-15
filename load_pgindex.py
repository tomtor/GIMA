#!/usr/bin/python3
# -*- coding: utf-8 -*-

import psycopg2
import sys


con = None

try:
    con = psycopg2.connect(database='gima', user='tom') 
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS documenten")
    cur.execute("CREATE TABLE documenten(id SERIAL PRIMARY KEY, doc TEXT, bron VARCHAR(100))")

    doc = ''
    count = 0
    f = open('data/geboorte.txt', 'r')
    for line in f:
        if len(line) == 1:
            count = count + 1
            doc = doc.translate(str.maketrans('', '', '"\''))
            #print(doc)
            print(count)
            for i in range(0, 1000):
                cur.execute("INSERT INTO documenten(doc,bron) VALUES('" \
                    + doc + "', 'demo')")
            doc = ''
        else:
            doc = doc + line
        con.commit()
    f.close()

    cur.execute("CREATE INDEX documenten_idx ON documenten USING gin(to_tsvector('dutch', doc))")
    con.commit()

    con.set_isolation_level(0)
    cur.execute("VACUUM")
    
except psycopg2.DatabaseError as e:
    print('Error %s' % e)
    sys.exit(1)
    
finally:
    if con:
        con.close()
