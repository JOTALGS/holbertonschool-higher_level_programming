#!/usr/bin/python3
"""dsdsdd sds ds dsd """

if __name__ == "__main__":
    """,ain fun ca"""
    import MySQLdb
    import sys
    user_name = sys.argv[1]
    user_passw = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user_name,
        passwd=user_passw,
        db=db_name
        )
    cur = db.cursor()
    qry = "SELECT * FROM states WHERE \
        name LIKE '{}' ORDER BY id ASC".format(state_name)
    cur.execute(qry)
    states = cur.fetchall()
    for state in states:
        print(state)

    db.close()
