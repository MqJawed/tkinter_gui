from tkinter import *

root = Tk()

root.title("Admission form")
root.geometry("499x600")

h1= Label(root,text="St.Thomas' College of Engineering and Technology",
     font="Georgian 12 bold").grid(row=0,column=0,columnspan=4,padx=15,pady=15,)

l1 = Label(root,text="Name",font="Helvetica 12")
l1.grid(row=1,column=0)
l2 = Label(root,text="Gender",font="Helvetica 12")
l2.grid(row=2,column=0)

nameval = StringVar()
genderval = StringVar()
checkval = IntVar()

e1=Entry(root,textvariable=nameval).grid(row=1,column=1)
e2=Entry(root,textvariable=genderval).grid(row=2,column=1)
c1 = Checkbutton(text="Disablity",variable=checkval).grid(row=3,column=1)

root.mainloop()