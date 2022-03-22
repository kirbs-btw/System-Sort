import tkinter as tk
from roundPolygon import *

mainColor = '#0f0f0f'
secColor = '#202020'
greyAccentColor = '#8E8E8E'
accentColor = '#599fd7'
textColor = '#ffffff'

def move_window(event, root):
    root.geometry('+{0}+{1}'.format(event.x_root, event.y_root))

def main():
    root = tk.Tk()

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

    canvas = tk.Canvas(root, height=500, width=500, bg=mainColor, highlightthickness=0)
    canvas.pack()

    rectangle = roundPolygon([25, 475, 475, 25], [100, 100, 475, 475], 10, canvas, width=5, fill=secColor)

    root.mainloop()

if __name__ == '__main__':
    main()


