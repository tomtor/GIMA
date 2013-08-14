#!/usr/bin/python3
# -*- coding: utf-8 -*-

import psycopg2
import sys


con = None

try:
    con = psycopg2.connect(database='gima', user='tom') 
    cur = con.cursor()

    cur.execute("DROP TABLE documenten")
    cur.execute("CREATE TABLE documenten(id SERIAL PRIMARY KEY, doc TEXT, bron VARCHAR(100))")

    doc = ''
    f = open('data/geboorte.txt', 'r')
    for line in f:
        if len(line) == 1:
            doc = doc.translate(str.maketrans('', '', '"\''))
            print(doc)
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
