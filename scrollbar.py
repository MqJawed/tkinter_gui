from tkinter import *

root = Tk()
root.geometry("444x222")

#creating a scrollbar
scrollbar = Scrollbar()
scrollbar.pack(side=RIGHT,fill="y")

#linking scrollbar
#1.in the class command (yscrollcommand=scrollbar.set)
#2.scrollbar.config(command = widget.yview)

lbx = Listbox(root,yscrollcommand=scrollbar.set)#1

for i in range(344):
    lbx.insert(END,i)
lbx.pack()

scrollbar.config(command = lbx.yview)#2

root.mainloop()