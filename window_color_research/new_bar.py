#custom title bar for tkinter

from tkinter import Tk, Frame, Button, Canvas

def move_window(event):
    root.geometry('+{0}+{1}'.format(event.x_root, event.y_root))

def main():
    root = Tk()

    root.overrideredirect(True) # turns off title bar, geometry
    root.geometry('400x100+200+200') # set new geometry

    # make a frame for the title bar
    title_bar = Frame(root, bg='blue', relief='raised', bd=0)

    # put a close button on the title bar
    close_button = Button(title_bar, text='Close this Window', command=root.destroy, bd = 0)

    # a canvas for the main area of the window
    window = Canvas(root, bg='black')

    # pack the widgets
    title_bar.pack(expand=1, fill="x")
    close_button.pack(side="right")
    window.pack(expand=1, fill="both")

    # bind title bar motion to the move window function
    title_bar.bind('<B1-Motion>', move_window)

    root.mainloop()

if __name__ == '__main__':
    main()

# credits atlasologist on stack overflow <3- https://stackoverflow.com/users/3275008/atlasologist