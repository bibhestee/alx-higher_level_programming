#!/usr/bin/python3
"""
    This is a script that lists all states with a name
    starting with N(Upper N) from the database hbtn_0e_0_usa
    using MySQLdb
"""


def filter_states():
    """
        Function that filter and print the states
    """
    import MySQLdb
    import sys
    MY_USER = sys.argv[1]
    MY_PASS = sys.argv[2]
    MY_DB = sys.argv[3]

    database = MySQLdb.connect(user=MY_USER, passwd=MY_PASS, db=MY_DB)
    cur = database.cursor()
    cur.execute("""SELECT * FROM states
    WHERE name LIKE 'N%' ORDER BY states.id ASC;""")
    items = cur.fetchall()
    for item in items:
        if item[1][0] == 'N':
            print(item)
    cur.close()
    database.close()


if __name__ == "__main__":
    filter_states()
