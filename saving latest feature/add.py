import sqlite3
from datetime import datetime


def addLatest(id):
    date = datetime.today().strftime('%Y-%m-%d')
    time = datetime.today().strftime('%H:%M:%S')

    conn = sqlite3.connect("test.sql")
    cur = conn.cursor()

    command = f"INSERT INTO latest VALUES('{id}', '{date}', '{time}')"
    cur.execute(command)
    conn.commit()


def checkTable(table):
    conn = sqlite3.connect("test.sql")
    cur = conn.cursor()
    command = f"SELECT * FROM {table}"
    out = cur.execute(command).fetchall()
    print(out)


def outLatest():
    conn = sqlite3.connect("test.sql")
    cur = conn.cursor()
    command = f"SELECT DISTINCT project_id FROM latest ORDER BY date"
    out = cur.execute(command).fetchall()
    # print(out)
    latestList = []

    if len(out) >= 10:
        latestList = out[:10]
        print(latestList)
    else:
        latestList = out
        print(latestList)

if __name__ == '__main__':
    outLatest()
    # addLatest(5)
    # checkTable("latest")
