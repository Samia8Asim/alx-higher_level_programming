#!/usr/bin/python3
"""lists all states from the database safe from MySQL injections"""
import MySQLdb
from sys import argv

if __name__ == "__main__":

    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s\
                ORDER BY id ASC", [argv[4]])

    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    conn.close()
