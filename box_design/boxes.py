import tkinter as tk
from tkinter import ttk

class window:
    def __init__(self):
        self.bgCol = "#4e4e4e"

    def window(self):
        self.root = tk.Tk()

        self.canvas = tk.Canvas(height=500, width=500, bg='#1e1e1e', highlightthickness=0)
        self.canvas.pack()

        self.table = tk.Canvas(self.canvas, bg=self.bgCol, highlightthickness=0)
        self.table.place(relx=0.05, rely=0.3, relwidth=0.9, relheight=0.65, anchor='nw')


        ## scrollbar stuff
        # create a main frame
        self.mainFrame = tk.Frame(self.table, bg=self.bgCol, highlightthickness=0)
        self.mainFrame.pack(fill='both', expand=1)
        # canvas
        self.visCanvas = tk.Canvas(self.mainFrame, bg=self.bgCol, highlightthickness=0)
        self.visCanvas.pack(side='left', fill='both', expand=1)
        # scrollbar
        self.canvScroll = ttk.Scrollbar(self.mainFrame, orient='vertical', command=self.visCanvas.yview)
        self.canvScroll.pack(side='right', fill='y')
        # cofig canvas
        self.visCanvas.configure(yscrollcommand=self.canvScroll.set)
        self.visCanvas.bind('<Configure>', lambda e: self.visCanvas.configure(scrollregion=self.visCanvas.bbox("all")))
        # create another frame in canvas
        self.frameInner = tk.Frame(self.visCanvas, bg=self.bgCol, highlightthickness=0)
        # add fram to window in canvas
        self.visCanvas.create_window((0, 0), window=self.frameInner, anchor="nw")
        ##################################################################################################

        self.insertBoxes()

        self.root.mainloop()

    def insertBoxes(self):
        for i in range(100):
            div = tk.Canvas(self.frameInner, bg="#f2f2f2", width=400, height=50, highlightthickness=0)
            div.grid(row=i, pady=(10, 0), padx=10)

            projectButton = tk.Button(div, text="Project 1", bg="#ffffff", bd=0)
            projectButton.place(relx=0.025, rely=0.25, relheight=0.5)

            entry = tk.Entry(div, justify='left', bd=0, bg="#f2f2f2")
            entry.place(relx=0.2, rely=0.25, relwidth=0.575, relheight=0.5)
            entry.insert("end", "stuff and stuff")

            dateLabel = tk.Label(div, text="2022-05-21", bg="#f2f2f2")
            dateLabel.place(relx=0.8, rely=0.25,  relheight=0.5)

main = window()
main.window()