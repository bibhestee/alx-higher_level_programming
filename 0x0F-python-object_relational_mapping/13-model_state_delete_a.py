#!/usr/bin/python3
"""
    This is a script that that deletes all State objects
        with a name containing the letter a
        from the database hbtn_0e_6_usa
"""


def model_state_update_id_2():
    """
        Function:
            This function creates an engine
            then connect to the database passed by the user
            then create a session to manage the data in
            the database.
            Deletes all object with letter a
    """
    import sys
    from model_state import Base, State
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import delete
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
    query = delete(State).where(State.name.like('%a%'))
    engine.execute(query)
    # query = session.query(State).filter(State.name.like('%a%')).all()
    session.close()


if __name__ == "__main__":
    model_state_update_id_2()
