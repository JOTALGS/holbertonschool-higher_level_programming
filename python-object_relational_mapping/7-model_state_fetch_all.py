#!/usr/bin/python3
"""
    sadarfeafewfwet  v gr gefg f afdsf sdg feaa dsf sdf
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name_ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1],
        sys.atgv[2],
        sys.argv[3]
    ))

    sess = sessionmaker(bind=engine)
    Session = sess()
    session = Session()
    result = session.query(State).order_by(State.id)

    for resu in result:
        print(resu)
