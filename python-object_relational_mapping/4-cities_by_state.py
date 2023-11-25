#!/usr/bin/python3
"""Module to list all states from database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """Function to list all states from database hbtn_0e_0_usa"""

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()

    cur.execute("SELECT cities.id, cities.name,\
                states.name FROM cities INNER JOIN states ON\
                cities.state_id = states.id ORDER BY cities.id")

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
