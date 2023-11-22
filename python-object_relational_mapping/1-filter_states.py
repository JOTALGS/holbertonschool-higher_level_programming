#!/usr/bin/python3
"""dsdsdd sds ds dsd """
if __name__ == "__main__":
    """,ain fun ca"""
    import MySQLdb
    import sys
    user_name = sys.argv[1]
    user_passw = sys.argv[2]
    db_name = sys.argv[3]
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user_name,
        passwd=user_passw,
        db=db_name
        )
    cur = db.cursor()
    qry = "SELECT * FROM states WHERE name LIKE '%N%' ORDER BY states.id ASC"
    cur.execute(qry)
    states = cur.fetchall()
    for state in states:
        if state[1][0] == 'N':
            print(state)
    db.close()
