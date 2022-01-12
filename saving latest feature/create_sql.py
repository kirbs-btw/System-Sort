import sqlite3

def createSql():
    #f = open("test.sql", "w+")
    conn = sqlite3.connect("test.sql")

    command = f"CREATE TABLE latest(project_id int, date date, time varchar(8))"
    conn.execute(command)
    conn.commit()

if __name__ == '__main__':
    createSql()