#!/usr/bin/python3
"""
  This is a script that lists all states from the database hbtn_0e_0_usa
    using MySQLdb ORM
"""


def select_cities(MY_USER, MY_PASS, MY_DB):
    """ Function that print the states """
    import MySQLdb

    database = MySQLdb.connect(user=MY_USER, passwd=MY_PASS, db=MY_DB)
    cur = database.cursor()
    query = """SELECT cities.id, cities.name, states.name
    FROM cities
    INNER JOIN states
    ON states.id = cities.state_id
    ORDER BY cities.id ASC;
    """
    cur.execute(query)
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
    select_cities(usr, pwd, db)
