import sqlite3

def main():
    """
    creates a sql file with the table mode

    to toggle between dark-mode and normal mode
    """
    #f = open("db.sql", "w+")
    conn = sqlite3.connect("mode.sql")
    cur = conn.cursor()

    command = "CREATE TABLE mode(mode VARCHAR(10))"
    cur.execute(command)
    conn.commit()

def add():
    """
    adds an item to the sql file
    """
    conn = sqlite3.connect("mode.sql")
    cur = conn.cursor()

    command = "INSERT INTO mode VALUES('nrml')"
    cur.execute(command)

    conn.commit()

def update():
    """
    updates the table
    switch between darkmode -> drkmd
    and normal ->nrml
    :return:
    """

    conn = sqlite3.connect("mode.sql")
    cur = conn.cursor()

    mode = "nrml"
    #mode = "drkmd"

    command = f"UPDATE mode SET mode = '{mode}'"
    cur.execute(command)

    conn.commit()


def printTable():
    """
    prints the table for debug
    :return:
    """
    conn = sqlite3.connect("mode.sql")
    cur = conn.cursor()

    command = "SELECT * FROM mode"
    table = cur.execute(command).fetchall()[0]

    print(table[0])


if __name__ == '__main__':
    update()
    printTable()