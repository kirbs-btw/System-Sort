import sqlite3

def convPath():
    """converts Path Table"""
    print("convPath")
    conn = sqlite3.connect("db.sql")
    cur = conn.cursor()
    table = cur.execute("SELECT * FROM folderPath").fetchall()

    conn2 = sqlite3.connect("other-db.sql")
    cur2 = conn2.cursor()

    for i in table:
        command = f"INSERT INTO folderPath VALUES({i[0]}, '{i[1]}')"
        print(command)
        cur2.execute(command)
        conn2.commit()

    conn.close()
    conn2.close()
    pass

def convfileTable():
    """converts filetable Table"""
    print("convfileTable")
    conn = sqlite3.connect("db.sql")
    cur = conn.cursor()
    table = cur.execute("SELECT * FROM fileTable").fetchall()

    conn2 = sqlite3.connect("other-db.sql")
    cur2 = conn2.cursor()

    for i in table:
        command = f"INSERT INTO fileTable VALUES({i[0]}, '{i[1]}', '{i[2]}', '{i[3]}', '{i[4]}')"
        print(command)
        cur2.execute(command)
        conn2.commit()

    conn.close()
    conn2.close()

def convfolderType():
    """converts FolderType Table"""
    print("convfolderType")
    conn = sqlite3.connect("db.sql")
    cur = conn.cursor()
    table = cur.execute("SELECT * FROM folderType").fetchall()

    conn2 = sqlite3.connect("other-db.sql")
    cur2 = conn2.cursor()

    for i in table:
        command = f"INSERT INTO folderType VALUES({i[0]}, '{i[1]}')"
        print(command)
        cur2.execute(command)
        conn2.commit()

    conn.close()
    conn2.close()

def convfolderNum():
    """converts FolderNum Table"""
    print("convfolderNum")
    conn = sqlite3.connect("db.sql")
    cur = conn.cursor()
    table = cur.execute("SELECT * FROM folderNum").fetchall()

    conn2 = sqlite3.connect("other-db.sql")
    cur2 = conn2.cursor()

    for i in table:
        command = f"INSERT INTO folderNum VALUES({i[0]}, {i[1]})"
        print(command)
        cur2.execute(command)
        conn2.commit()

    conn.close()
    conn2.close()

def delTable():
    """clears Tables"""
    conn = sqlite3.connect("other-db.sql")
    cur = conn.cursor()
    cur.execute("DELETE FROM folderPath")
    conn.commit()
    cur.execute("DELETE FROM fileTable")
    conn.commit()
    cur.execute("DELETE FROM folderType")
    conn.commit()
    cur.execute("DELETE FROM folderNum")
    conn.commit()
    conn.close()

if __name__ == '__main__':
    #
    #execution Line
    #

    #delTable()
    convPath()
    convfileTable()
    convfolderType()
    convfolderNum()

#creadit Bastian Lipka