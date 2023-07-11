from tkinter import *
def getval():
    print(userval.get())
    print(passval.get())
    file = open("user1.txt","a") # in append mode so the data will not be overwritten
    file.write(f"User Name = {userval.get()}") #write takes only string so userval.get()
    file.write(f"\nPassword = {passval.get()}\n\n")
    file.close()

root = Tk()

root.geometry("777x444")

user = Label(root, text="UserName")
user.grid() #instead of pack grid to get row column || default row column is 0

password= Label(root, text= "Password")
password.grid(row=1)

#types of entry widget variable
#StringVar,IntVar, BooleanVar,DoubleVar

#entry widget
#userentry = Entry(root, textvariable=StringVar)
#passentry = Entry(root, textvariable=StringVar)

#we are taking a variable to access the data of entry widget entered by the user
userval=StringVar()
passval = StringVar()

userentry = Entry(root, textvariable=userval)
passentry = Entry(root, textvariable=passval)
userentry.grid(row = 0,column =1)
passentry.grid(row = 1,column =1)

#one liner be familiar
#Button(text = "Submit", font="bold",command=getval).grid(row=2,column=1)

#another way of one liner when b1 is required
#b1 = Button(text = "Submit", font="bold",command=getval()).grid(row=2,column=1)

#dont use one liner when it got more job see Event.py
#b1.bind not working when not b1.pack()

b1 = Button(text = "Submit", font="bold",command=getval)
b1.grid(row=2,column=1)

root.mainloop()