from tkinter import *
import tkinter.messagebox as tmsg

def getdollar():
    tmsg.showinfo("HURRAY",f"We have credited {slide.get()} dollar amount in your account")

root = Tk()

root.geometry("444x222")

slide = Scale(root, from_=0 ,to= 100,orient= HORIZONTAL,tickinterval=50)
slide.set(25) # setting the initial value
slide.pack()

b1=Button(text="Get Dollar",command=getdollar,pady=15).pack(pady=50)

root.mainloop()