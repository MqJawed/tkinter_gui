from tkinter import *

root = Tk()

#root.geometry("777x345")
f1 = Frame(root, bg = "red",borderwidth=5,relief=RAISED)
f1.pack(fill=Y)

l1 = Label(f1, text = "HELLO",padx=56,pady=90)
l1.pack(padx=56,pady=90)

root.mainloop()