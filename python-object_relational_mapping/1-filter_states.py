#!/usr/bin/python3
"""Module to list all states from database hbtn_0e_0_usa starting with N"""

import MySQLdb
import sys

if __name__ == "__main__":
    """Function to list all states from database hbtn_0e_0_usa starting with N"""

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")

    rows = cur.fetchall()
    for row in rows:
        if row[1][0] == 'N':
            print(row)

    cur.close()
    db.close()
