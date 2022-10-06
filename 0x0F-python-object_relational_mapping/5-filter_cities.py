#!/usr/bin/python3
"""
    This is a script that lists all cities of states filter
    by argument passed from the database hbtn_0e_0_usa
    using MySQLdb ORM
"""


def filter_cities(MY_USER, MY_PASS, MY_DB, STATE_NAME):
    """ Function that print the states """
    import MySQLdb

    database = MySQLdb.connect(user=MY_USER, passwd=MY_PASS, db=MY_DB)
    cur = database.cursor()
    query = '''SELECT name FROM cities
    WHERE state_id = (SELECT id FROM states WHERE
    name = \'{}\') ORDER BY cities.id ASC;'''.format(STATE_NAME)
    cur.execute(query)
    items = cur.fetchall()
    pack = ()
    for item in items:
        pack += item
    unpack = ', '.join(pack)
    print(unpack)
    cur.close()
    database.close()


if __name__ == "__main__":
    import sys
    usr = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    st = sys.argv[4]
    if (st.__contains__('TRUNCATE' or 'FROM' or 'SELECT')):
        st = ''
    filter_cities(usr, pwd, db, st)
