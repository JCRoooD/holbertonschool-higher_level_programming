#!/usr/bin/python3
"""Module to list all states from database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """Function to list all states from database hbtn_0e_0_usa"""

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()

    cur.execute("SELECT name FROM cities WHERE state_id = \
                (SELECT id FROM states WHERE name = '{}')\
                ORDER BY id".format(argv[4]))

    rows = cur.fetchall()
    tabla = []
    for row in rows:
        tabla.append(row[0])
    print(', '.join(tabla))

    cur.close()
    db.close()
    