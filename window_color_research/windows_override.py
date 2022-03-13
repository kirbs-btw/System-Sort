import tkinter as tk
from tkinter import ttk
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


def main():
    root = tk.Tk()
    root.geometry('500x500')
    root.resizable(0, 0)
    root.title("Window Config")

    dark_title_bar(root)
    # root.overrideredirect(True)

    root.mainloop()





if __name__ == '__main__':
    main()

# thanks to Konstantin Ehmann from Stack overflow <3 - https://stackoverflow.com/users/17942637/konstantin-ehmann
