#!/usr/bin/python3
"""dsdsdd sds ds dsd """

if __name__ == '__main__':
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    import sys

    ny_usrn = sys.argv[1]
    my_passw = sys.argv[2]
    my_db = sys.argv[3]
    engstr = f'mysql+mysqldb:///{my_usrn}:{my_passw}@localhost:3306/{my_db}'
    engine = create_engine(engstr)

    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id)

    for state in states:
        print(state)
