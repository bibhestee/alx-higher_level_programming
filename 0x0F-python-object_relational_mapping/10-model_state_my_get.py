#!/usr/bin/python3
"""
    This script prints the State object with the name passed as argument
    from the database hbtn_0e_6_usa
"""


def model_state_my_get():
    """
        This function connects to the database, create session
        and prints the objects with the name passed.
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
    arg_4 = sys.argv[4]
    if (arg_4.__contains__('TRUNCATE' or 'FROM' or 'SELECT')):
        arg_4 = ''

    # An Engine, which the Session will use for connection resources
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            arg_1, arg_2, arg_3, pool_pre_ping=True))
    # Activate the engine with Base Class
    Base.metadata.create_all(engine)

    # Configure the session class
    Session.configure(bind=engine)

    # Create a Session
    session = Session()
    query = session.query(State).filter_by(name=arg_4).order_by(State.id).all()
    if query == []:
        print('Not found')
    else:
        for state in query:
            print(state.id)
    session.close()


if __name__ == "__main__":
    model_state_my_get()
