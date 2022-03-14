Styling the head of a window:

In tkinter...
there are three methods i found:

1. The seemingly easy one!

    ---
    root = tk.Tk()
    root.configure(bg='black') <--
    root.mainloop()
    ---

    so you should be able to just configure the root and change the
    color of your window right?
    No!
    It changes the background of the window but not the head :)
    (at least for me, i have seen some people where it worked)

    thanks to Dev Prakash Sharma
    https://www.tutorialspoint.com/changing-the-background-color-of-a-tkinter-window-using-colorchooser-module

2. The pretty weird version:

    You can hard force the windows setting to dark-mode but only for this window.
    Should be easy right?
    No!

    Code excerpt:

    ---

    import ctypes as ct

    def dark_title_bar(window):
    """
    MORE INFO:
    https://docs.microsoft.com/en-us/windows/win32/api/dwmapi/ne-dwmapi-dwmwindowattribute
    """
    window.update()
    DWMWA_USE_IMMERSIVE_DARK_MODE = 20
    set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
    get_parent = ct.windll.user32.GetParent
    hwnd = get_parent(window.winfo_id())
    rendering_policy = DWMWA_USE_IMMERSIVE_DARK_MODE
    value = 2
    value = ct.c_int(value)
    set_window_attribute(hwnd, rendering_policy, ct.byref(value),
                         ct.sizeof(value))

    ---
    thanks to Konstantin Ehmann from Stack overflow <3
    https://stackoverflow.com/users/17942637/konstantin-ehmann

    but it did only somewhat work...

    it changes the color to black but only if you make the window small and then open it up again
    and only after this it changed :)

3. The totally dumb solution - i'm gonna use it :) :
    you can go and just delete the whole bar and create a new one :)
    it's a bit 'glitchy' but it's okay

    code excerpt:

    ---
    from tkinter import Tk, Frame, Button, Canvas

    root = Tk()

    def move_window(event):
        root.geometry('+{0}+{1}'.format(event.x_root, event.y_root))

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

    ---

    thanks to atlasologist on stack overflow <3
    https://stackoverflow.com/users/3275008/atlasologist

    you can find the code to my rage in this folder <3

    Version 1: tk_version.py
    Version 2: windows_override.py
    Version 3: new_bar.py

    love to all the answers i found <3

    thanks to Dev Prakash Sharma - https://www.tutorialspoint.com/changing-the-background-color-of-a-tkinter-window-using-colorchooser-module
    thanks to Konstantin Ehmann from Stack overflow <3 - https://stackoverflow.com/users/17942637/konstantin-ehmann
    thanks to atlasologist on stack overflow <3- https://stackoverflow.com/users/3275008/atlasologist

