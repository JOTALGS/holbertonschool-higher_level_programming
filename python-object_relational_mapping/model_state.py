#!/usr/bin/python3
"""dsdsdd sds ds dsd """

if __name__ == "__main__":
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy import Column, Integer, String

    Base = declarative_base()

    class State(Base):
        """comne asdsds docu nadns ansdnsndjdd js dj"""
        __tablename__ = 'states'
        id = Column(Integer, autoincrement='auto',
                    unique=True, primary_key=True)
        name = Column(String(128))
