import tkinter as tk

colorTop = '#0f0f0f'


def move_window(event, root):
    root.geometry('+{0}+{1}'.format(event.x_root, event.y_root))
    # print(f"x{event.x_root}         y{event.y_root}")

def main():
    root = tk.Tk()

    systemSort_icon = tk.PhotoImage(file="icon.png")

    root.overrideredirect(True)  # turns off title bar, geometry
    root.geometry('+200+200') # places the window

    top_Bar = tk.Frame(root, bg=colorTop, relief='raised', bd=0)
    top_Bar.pack(expand=1, fill='x')

    close_button = tk.Button(top_Bar, text='x', font=("Gotham Black", 15), command = lambda: root.destroy(), bd=0, bg=colorTop, fg="#ffffff")
    close_button.pack(side="right")

    # test for an icon - not capacity to do it today - coming soon
    icon = tk.Label(top_Bar, image=systemSort_icon, bg=colorTop, fg="#ffffff")
    icon.pack(side="left", padx=10)

    # custom title
    title = tk.Label(top_Bar, text='test window', bg=colorTop, fg="#ffffff")
    title.pack(side="left", padx=10)

    # highlightthickness = 0 --> gets rid of ugly border

    # new main canvas - size of the new container
    canvas = tk.Canvas(root, width=500, height=500, bg='#202020', highlightthickness=0)
    canvas.pack(expand=1, fill='both')

    # bind the top bar so you can move it
    top_Bar.bind('<B1-Motion>', lambda event, arg=root: move_window(event, arg))

    root.mainloop()

if __name__ == '__main__':
    main()


