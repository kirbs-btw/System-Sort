import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, bg="#ff32ee", width=500, height=500)
canvas.pack()

table = tk.Canvas(canvas, bg='#eedeff')
table.place(relx=0.05, rely=0.3, relwidth=0.9, relheight=0.65, anchor='nw')

def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):
    points = [x1 + radius, y1,
              x1 + radius, y1,
              x2 - radius, y1,
              x2 - radius, y1,
              x2, y1,
              x2, y1 + radius,
              x2, y1 + radius,
              x2, y2 - radius,
              x2, y2 - radius,
              x2, y2,
              x2 - radius, y2,
              x2 - radius, y2,
              x1 + radius, y2,
              x1 + radius, y2,
              x1, y2,
              x1, y2 - radius,
              x1, y2 - radius,
              x1, y1 + radius,
              x1, y1 + radius,
              x1, y1]

    return table.create_polygon(points, **kwargs, smooth=True)


my_rectangle = round_rectangle(5, 5, 450, 100, radius=20, fill="blue")

root.mainloop()