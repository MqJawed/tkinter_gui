from tkinter import *

root = Tk()
def apply(widval,heival):
    can_width = widval
    can_hei = heival
    root.geometry(f"{can_width.get()}x{can_hei.get()}")#.geometry takes string val

#root.geometry("444x222")
l1 = Label(text="Enter width",font = "Georgian 8 bold",fg = "blue")
l1.grid(row=0,column=0,padx =15,pady=25)

l2 = Label(text="Enter Height",font = "Georgian 8 bold",fg = "blue")
l2.grid(row=1,column=0,padx =15,pady=25)

widval = IntVar()
heival = IntVar()

e1 = Entry(textvariable=widval).grid(row=0,column =1)
e2 = Entry(textvariable=heival).grid(row=1,column =1)

b1 = Button(text="Apply",bg = "green",fg = "white",command=lambda:apply(widval, heival))
b1.grid(row=2,column =0,padx=25,pady=15)
root.mainloop()