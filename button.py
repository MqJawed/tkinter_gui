from tkinter import *

root = Tk()

root.geometry("777x444")

def Print():
    print("Hello programmer")
def name():
    print("Mqjawed")

f1 = Frame(root,bg = "red",borderwidth=5, relief = SUNKEN)
f1.pack(side= LEFT,anchor = NW)

b1 = Button(f1,bg="grey",text="Print",font = "algerian 12 bold",padx=8,pady=9,
            command=Print)#only the function name
b1.pack(padx=9,pady=9)

f2 = Frame(root,bg = "green",borderwidth=5,relief="raised")
f2.pack(anchor="ne")

b2=Button(f2,bg = 'grey',text="name",font="Georgian 12 bold",padx = 8, pady=9,
          command=name)
b2.pack(padx=9,pady=9)

root.mainloop()