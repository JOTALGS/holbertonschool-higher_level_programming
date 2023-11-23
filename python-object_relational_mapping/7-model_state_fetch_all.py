#!/usr/bin/python3
"""dsdsdd sds ds dsd """

if __name__ == '__main__':
    from sqlalchemy import create_engine
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    import sys

    ny_usrn = sys.argv[1]
    my_passw = sys.argv[2]
    my_db = sys.argv[3]
    engine = create_engine(f'sqlite:///{my_usrn}:{my_passw}@localhost:3306/{my_db}')
    Base = declarative_base()

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(id)
    for state in states:
        print(state)
