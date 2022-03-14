import tkinter as tk

colorTop = '#5584c3'


def move_window(event, root):
    root.geometry('+{0}+{1}'.format(event.x_root, event.y_root))

def main():
    root = tk.Tk()

    root.overrideredirect(True)  # turns off title bar, geometry
    root.geometry('+200+200') # set new geometry

    top_Bar = tk.Frame(root, bg=colorTop, relief='raised', bd=0)
    top_Bar.pack(expand=1, fill='x')

    close_button = tk.Button(top_Bar, text='x', font=("Gotham Black", 15), command = lambda: root.destroy(), bd=0, bg=colorTop, fg="#ffffff")
    close_button.pack(side="right")

    # test for an icon - not capacity to do it today - coming soon
    title_test = tk.Label(top_Bar, text='hello there', bg=colorTop, fg="#ffffff")
    title_test.pack(side="left", padx=25)

    # custom title
    title = tk.Label(top_Bar, text='test window', bg=colorTop, fg="#ffffff")
    title.pack(side="left", padx=25)

    # new main canvas
    canvas = tk.Canvas(root, width=500, height=500, bg='blue')
    canvas.pack(expand=1, fill='both')

    # bind the top bar so you can move it
    top_Bar.bind('<B1-Motion>', lambda event, arg=root: move_window(event, arg))

    root.mainloop()

if __name__ == '__main__':
    main()


