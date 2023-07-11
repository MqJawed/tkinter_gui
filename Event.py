from tkinter import *

root = Tk()
def left(event):
    print("Left")
b1=Button(text="Click")
b1.pack() 

b1.bind('<Button-1>',left)


root.mainloop()