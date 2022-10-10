#!/usr/bin/python3
"""
    This is a script that lists all states with a name
    that matches the argument passed from the database hbtn_0e_0_usa
    using MySQLdb
"""


def my_filter_states(MY_USER, MY_PASS, MY_DB, NAME):
    """ Function that filter and print the states """
    import MySQLdb

    database = MySQLdb.connect(user=MY_USER, passwd=MY_PASS, db=MY_DB)
    cur = database.cursor()
    cur.execute("""SELECT * FROM states
    WHERE name = \'{}\' ORDER BY states.id ASC;""".format(NAME))
    items = cur.fetchall()
    for item in items:
        if item[1][0] == NAME[0]:
            print(item)
    cur.close()
    database.close()


if __name__ == "__main__":
    import sys
    usr = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    st = sys.argv[4]
    my_filter_states(usr, pwd, db, st)
