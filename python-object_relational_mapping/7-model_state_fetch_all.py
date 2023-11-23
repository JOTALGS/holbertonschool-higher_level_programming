#!/usr/bin/python3
"""dsdsdd sds ds dsd """


    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    import sys

if __name__ == '__main__':
    ny_usrn = sys.argv[1]
    my_passw = sys.argv[2]
    my_db = sys.argv[3]
    engstr = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        my_usrn,
        my_passw,
        my_db
    )
    engine = create_engine(engstr)

    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id).all()

    for state in states:
        print(state)
