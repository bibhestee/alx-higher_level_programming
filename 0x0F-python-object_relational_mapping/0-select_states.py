#!/usr/bin/python3
"""
  This is a script that lists all states from the database hbtn_0e_0_usa
    using MySQLdb ORM
"""


def select_states(MY_USER, MY_PASS, MY_DB):
    """ Function that print the states """
    import MySQLdb

    database = MySQLdb.connect(user=MY_USER, passwd=MY_PASS, db=MY_DB)
    cur = database.cursor()
    cur.execute("SELECT * FROM states")
    items = cur.fetchall()
    for item in items:
        print(item)
    cur.close()
    database.close()


if __name__ == "__main__":
    import sys
    usr = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    select_states(usr, pwd, db)
