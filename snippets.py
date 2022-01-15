import os
import tkinter as tk
from tkinter import ttk
from TkinterDnD2 import DND_FILES, TkinterDnD
import shutil
from openpyxl import load_workbook
from datetime import datetime
import time
from tkinter import filedialog
import sqlite3
import keyboard
import random

"""
Here are some snippets of the System Sort program to be found at kw-corp.de
Download now to try it out ! 


"""


def openFolderInTable(path):
    try:
        # path = os.path.realpath(path[2])
        os.startfile(path[2])
    except:
        conn = sqlite3.connect(db_conn_path)
        cur = conn.cursor()
        table = cur.execute(f'SELECT * FROM folderPath ORDER BY key').fetchall()[-1][1]
        otherPath = str(table) + "/" + str(path[1])
        os.startfile(otherPath)
    try:
        addLatest(path[0])
        print("added to latest!")
    except:
        print("failed to add!")


def addLatest(id):
    date = datetime.today().strftime('%Y-%m-%d')
    time = datetime.today().strftime('%H:%M:%S')

    conn = sqlite3.connect(db_conn_path)
    cur = conn.cursor()

    command = f"INSERT INTO latest VALUES('{id}', '{date}', '{time}')"
    cur.execute(command)
    conn.commit()


def outLatest(frame2):
    conn = sqlite3.connect(db_conn_path)
    cur = conn.cursor()
    command = f"SELECT DISTINCT project_id FROM latest ORDER BY date"
    out = cur.execute(command).fetchall()
    latestList = []

    for i in out:
        command = f"SELECT * FROM fileTable WHERE key = '{i[0]}'"
        row = cur.execute(command).fetchall()
        latestList.append(row[0])

    if len(out) >= 10:
        latestList = latestList[:10]

        printArrInTable(latestList, frame2)
    else:
        printArrInTable(latestList, frame2)

# credits Kirbs-btw - Bastian Lipka
