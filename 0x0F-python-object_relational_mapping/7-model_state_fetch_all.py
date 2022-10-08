#!/usr/bin/python3
"""
    This script lists all state objects from the database hbtn_0e_6_usa
"""


def model_state_fetch_all():
    """
        fetch all lists of state objects
    """
    import sys
    from model_state import Base, State
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
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    session.close()


if __name__ == "__main__":
    model_state_fetch_all()
