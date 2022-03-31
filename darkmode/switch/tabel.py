import sqlite3

def main():
    #f = open("db.sql", "w+")
    conn = sqlite3.connect("db.sql")
    cur = conn.cursor()

    command = "CREATE TABLE mode(mode VARCHAR(10))"
    cur.execute(command)
    conn.commit()

def add():
    conn = sqlite3.connect("db.sql")
    cur = conn.cursor()

    command = "INSERT INTO mode VALUES('nrml')"
    cur.execute(command)

    conn.commit()

def update():
    conn = sqlite3.connect("db.sql")
    cur = conn.cursor()

    mode = "nrml"
    mode = "drkmd"

    command = f"UPDATE mode SET mode = '{mode}'"
    cur.execute(command)

    conn.commit()


def printTable():
    conn = sqlite3.connect("db.sql")
    cur = conn.cursor()

    command = "SELECT * FROM mode"
    table = cur.execute(command).fetchall()[0]

    print(table[0])


if __name__ == '__main__':
    update()
    printTable()