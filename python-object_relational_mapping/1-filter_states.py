#!/usr/bin/python3
"""Module to list all states from database hbtn_0e_0_usa starting with N"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """Function to list all states from database starting with N"""

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")

    rows = cur.fetchall()
    for row in rows:
        if row[1][0] == 'N':
            print(row)

    cur.close()
    db.close()
