import tkinter as tk
from tkinter import colorchooser

def main():
    root = tk.Tk()

    root.geometry("700x350")

    label = tk.Label(root, text="This is a new Label text", font=('Arial 17 bold'))
    label.place(relx=0.5, rely=0.2, anchor = tk.CENTER)

    color = tk.colorchooser.askcolor()

    colorname=color[1]

    root.configure(background=colorname)
    root.mainloop()

    # src = https://www.tutorialspoint.com/changing-the-background-color-of-a-tkinter-window-using-colorchooser-module

if __name__ == '__main__':
    main()

# thanks to Dev Prakash Sharma - https://www.tutorialspoint.com/changing-the-background-color-of-a-tkinter-window-using-colorchooser-module