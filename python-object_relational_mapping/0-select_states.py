#!/usr/bin/python3
"""dsdsdd sds ds dsd """
import MySQLdb
import sys


def main():
    """,ain fun ca"""
    user_name = sys.argv[1]
    user_passw = sys.argv[2]
    db_name = sys.argv[3]
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=user_name,
        passwd=user_passw,
        db=db_name
        )
    cur = db.cursor()
    cur.execute('SELECT * FROM states ORDER BY id ASC')
    rows = cur.fetchall()
    for row in rows:
        print(row)
    db.close()


if __name__ == "__main__":
    main()
