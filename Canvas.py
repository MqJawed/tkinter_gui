from tkinter import *

root = Tk()

can_wid = 133  # to change the geometry easily
can_hei = 222

root.geometry(f"{can_wid}x{can_hei}")

can_widg = Canvas(root , width=can_wid,height=can_hei)
can_widg.pack()

#co ordinate of two points
can_widg.create_line(0,0,444,222)

#coordinate of top left and bottom right
can_widg.create_rectangle(23,44,88,99)

root.mainloop()
