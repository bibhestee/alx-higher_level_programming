#!/usr/bin/python3
"""
    This script prints all City objects from the database hbtn_0e_14_usa
"""


def model_city_fetch_by_state():
    """
        fetch all lists of city by state objects
    """
    import sys
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    # Create a "Session" class
    Session = sessionmaker()

    arg_1 = sys.argv[1]
    arg_2 = sys.argv[2]
    arg_3 = sys.argv[3]

    # An Engine, which the Session will use for connection resources
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            arg_1, arg_2, arg_3, pool_pre_ping=True))
    # Activate the engine with Base Class
    Base.metadata.create_all(engine)

    # Configure the session class
    Session.configure(bind=engine)

    # Create a Session
    session = Session()
    query = session.query(State, City).join(City).order_by(City.id).all()
    for states, cities in query:
        print("{}: ({}) {}".format(states.name, cities.id, cities.name))
    session.close()


if __name__ == "__main__":
    model_city_fetch_by_state()
