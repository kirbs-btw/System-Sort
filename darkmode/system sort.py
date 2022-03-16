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

#mainCol = "#ededed"
#green = "#69e750"
#mainColBlue = "#599fd7"
#accentColor = "#ea498b"
#lightBlue = "#a3d8e6"

db_conn_path = "db/db.sql"

mainColor = '#0f0f0f'
secColor = '#202020'
greyAccentColor = '#8E8E8E'
accentColor = '#599fd7'
textColor = '#ffffff'

class pathSave:

    def setPath(self, n):
        self.path = n

pathSaveObj = pathSave()
##################################################
# System Sort Window - Drag and Drop & Create Dir
##################################################

##window function
def drop_inside_list_box(event, arg):
    pathSaveObj.setPath(event.data)
    arg.insert("end", event.data)


# event.data == file path
# if multiple file path it´s one string and has to be separated
##################################################
def move_window(event, root):
    root.geometry('+{0}+{1}'.format(event.x_root, event.y_root))

def mainApp():
    root = TkinterDnD.Tk()
    #root.iconbitmap('gui/system_sorter.ico')
    #root.title('System Sorter')

    systemSort_icon = tk.PhotoImage(file="gui/icon.png")

    root.overrideredirect(True)  # turns off title bar, geometry
    root.geometry('+200+200')  # places the window

    top_Bar = tk.Frame(root, bg=mainColor, relief='raised', bd=0)
    top_Bar.pack(expand=1, fill='x')

    close_button = tk.Button(top_Bar, text='x', font=("Gotham Black", 15), command=lambda: root.destroy(), bd=0,
                             bg=mainColor, fg="#ffffff")
    close_button.pack(side="right")

    icon = tk.Label(top_Bar, image=systemSort_icon, bg=mainColor, fg="#ffffff")
    icon.pack(side="left", padx=10)

    title = tk.Label(top_Bar, text='System Sort', bg=mainColor, fg="#ffffff")
    title.pack(side="left", padx=10)

    top_Bar.bind('<B1-Motion>', lambda event, arg=root: move_window(event, arg))

    #backgoundImage = tk.PhotoImage(file='gui/bg.png')
    settingsImg = tk.PhotoImage(file='gui/settings.png')
    glassImg = tk.PhotoImage(file='gui/glass.png')

    canvas = tk.Canvas(root, width=500, height=500, highlightthickness=0, bg=mainColor)
    canvas.pack(expand=1, fill='both')

    #canvas.create_image(0, 0, image=backgoundImage, anchor="nw")

    canvas.create_text(250, 25, text="System Sort", fill=textColor, font=("Gotham Black", 25), anchor="n")

    # dnd input
    dnd_menu = tk.Listbox(canvas, selectmode=tk.SINGLE, background=secColor, bd=0, highlightthickness=0)
    dnd_menu.place(relx=0.05, rely=0.3, relwidth=0.9, relheight=0.65, anchor='nw')

    dnd_menu.drop_target_register(DND_FILES)
    dnd_menu.dnd_bind("<<Drop>>", lambda event, arg=dnd_menu: drop_inside_list_box(event, arg))

    # button
    create = tk.Button(canvas, text="create folder", bg=accentColor, fg="white", bd=0)
    create.place(relx=0.7, rely=0.2, relwidth=0.25, relheight=0.05, anchor="nw")

    canvas.create_text(30, 90, text="Content: ", fill=greyAccentColor, anchor="w")

    # input
    content = tk.Entry(canvas, bd=0, justify="left", bg=secColor, fg=textColor)
    content.place(relx=0.05, rely=0.2, relwidth=0.6, relheight=0.05, anchor="nw")

    dndLable = tk.Label(canvas, text="Drop folders here!", justify="center", fg=greyAccentColor, bg=secColor)

    dndLable.config(font=("Gotham Black", 20))
    dndLable.place(relx=0.25, rely=0.8, relwidth=0.5, relheight=0.1, anchor='nw')

    changeConfig = tk.Button(canvas, image=settingsImg, borderwidth=0, bg=mainColor)
    changeConfig.place(relx=0.05, rely=0.05, relwidth=0.072, relheight=0.072, anchor="nw")

    searchFolder = tk.Button(canvas, image=glassImg, borderwidth=0, bg=mainColor)
    searchFolder.place(relx=0.878, rely=0.05, relwidth=0.072, relheight=0.072, anchor="nw")

    root.mainloop()

mainApp()

# Bastian Nicholas Lipka -lipka.bastian04@gmail.com - V-1.1.0
