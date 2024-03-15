#!/usr/bin/python3
"""script to lists all states from the database hbtn_0e_0_usa start with N"""
import MySQLdb
from sys import argv

if __name__ == "__main__":

    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    sql_query = "SELECT * FROM states WHERE name\
                LIKE BINARY '{}' ORDER BY id ASC".format(argv[4])
    cur.execute(sql_query)

    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    conn.close()
