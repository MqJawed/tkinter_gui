from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("444x222")

def submit():
    tmsg.showinfo("YaHoO!",f"You have chosen {radiobutton_var.get()} as your favourite")
    

radiobutton_var = StringVar()
radiobutton_var.set(0) #initally that value will be selected which is given in set

Label(text="Which is your favourite animal?",font="lucida 19 bold").pack(pady=15)

radio = Radiobutton(text="Tiger",font="12",variable=radiobutton_var,value="Tiger")
radio.pack(anchor=W)
radio = Radiobutton(text="Lion",font="12",variable=radiobutton_var,value="Lion")
radio.pack(anchor="w")
radio = Radiobutton(text="Giraffe",font="12",variable=radiobutton_var,value="Giraffe")
radio.pack(anchor="w")
radio = Radiobutton(text="Duck",font="12",variable=radiobutton_var,value="Duck")
radio.pack(anchor="w")

b1 = Button(text="Submit",font="lucida 12 bold",pady=10,command=submit)
b1.pack(pady=10)

root.mainloop()

#first run the program...we don't use radiobutton_var as string var and value 
# as string rather integer and we make function to transform that