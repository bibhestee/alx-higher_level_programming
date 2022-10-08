#!/usr/bin/python3
"""
    This is a script that adds the State object "Lousiana" to
    the database
"""


def model_state_insert():
    """
        Function:
            This function creates an engine
            then connect to the database passed by the user
            then create a session to manage the data in
            the database.
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
    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    query = session.query(State).filter_by(name='Louisiana').all()
    print(query[-1].id)
    session.close()


if __name__ == "__main__":
    model_state_insert()
