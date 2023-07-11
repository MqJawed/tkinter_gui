from tkinter import *

def add():
    global i
    lbx.insert(END,i)
    i+=1
i=0
root = Tk()
root.geometry("444x222")
lbx = Listbox()
lbx.insert(END,"fist element")
lbx.pack()

b1 = Button(text="ADD ITEM",command=add)
b1.pack()

root.mainloop()

# End index = after the selected element
# Active index = before the selected element
