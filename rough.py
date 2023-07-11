from tkinter import *


root = Tk()
root.geometry("333x466")
root.maxsize(333,444)
root.title("Calculator")
root.wm_iconbitmap("ico.ico")
root.configure(background="grey")

def click(event):
    global value
    text = event.widget.cget("text") #to get the value of that widget
    print(text)
    if text == "=":
        if value.get().isdigit():
            calval = int(value.get())
        else:
            try:
                calval = eval(show.get())
                value.set(calval)
                #show.update()
            except:
                value.set("Error")
    elif text == "AC":
        value.set("")
        
    elif text == "Del":
        delv = value.get()
        newval = delv[0:-1]
        value.set(newval)
        
    else:
        value.set(value.get()+text)

value = StringVar()
value.set("")


show = Entry(root,textvariable=value,font="Helvetica 30",width=15)
show.pack(anchor="w",ipady=5,padx=5,pady=15)

f1 = Frame(root,bg="grey")
f1.pack(anchor="w",padx=5 ,pady=5)

b1 = Button(f1,text="7",font="lucida 25 bold",relief=SUNKEN,width=3,bg="cyan")
b1.pack(side="left",padx=5)
b1.bind('<Button-1>',click)
b2 = Button(f1,text="8",font="lucida 25 bold",relief=SUNKEN,width=3,bg="cyan")
b2.pack(side="left",padx=5)
b2.bind('<Button-1>',click)
b3 = Button(f1,text="9",font="lucida 25 bold",relief=SUNKEN,width=3,bg="cyan")
b3.pack(side="left",padx=5)
b3.bind('<Button-1>',click)
b4 = Button(f1,text="+",font="lucida 25 bold",relief=SUNKEN,width=3,bg="magenta")
b4.pack(side="left",padx=5)
b4.bind('<Button-1>',click)

f1 = Frame(root,bg="grey")
f1.pack(anchor="w",padx=5 ,pady=5)

b1 = Button(f1,text="4",font="lucida 25 bold",relief=SUNKEN,width=3,bg="cyan")
b1.pack(side="left",padx=5)
b1.bind('<Button-1>',click)
b2 = Button(f1,text="5",font="lucida 25 bold",relief=SUNKEN,width=3,bg="cyan")
b2.pack(side="left",padx=5)
b2.bind('<Button-1>',click)
b3 = Button(f1,text="6",font="lucida 25 bold",relief=SUNKEN,width=3,bg="cyan")
b3.pack(side="left",padx=5)
b3.bind('<Button-1>',click)
b4 = Button(f1,text="-",font="lucida 25 bold",relief=SUNKEN,width=3,bg="magenta")
b4.pack(side="left",padx=5)
b4.bind('<Button-1>',click)

f1 = Frame(root,bg="grey")
f1.pack(anchor="w",padx=5 ,pady=5)

b5 = Button(f1,text="1",font="lucida 25 bold",relief=SUNKEN,width=3,bg="cyan")
b5.pack(side="left",padx=5)
b5.bind('<Button-1>',click)
b6 = Button(f1,text="2",font="lucida 25 bold",relief=SUNKEN,width=3,bg="cyan")
b6.pack(side="left",padx=5)
b6.bind('<Button-1>',click)
b7 = Button(f1,text="3",font="lucida 25 bold",relief=SUNKEN,width=3,bg="cyan")
b7.pack(side="left",padx=5)
b7.bind('<Button-1>',click)
b8 = Button(f1,text="/",font="lucida 25 bold",relief=SUNKEN,width=3,bg="magenta")
b8.pack(side="left",padx=5)
b8.bind('<Button-1>',click)

f1 = Frame(root,bg="grey")
f1.pack(anchor="w",padx=5 ,pady=5)

b5 = Button(f1,text="0",font="lucida 25 bold",relief=SUNKEN,width=3,bg="cyan")
b5.pack(side="left",padx=5)
b5.bind('<Button-1>',click)
b6 = Button(f1,text=".",font="lucida 25 bold",relief=SUNKEN,width=3,bg="cyan")
b6.pack(side="left",padx=5)
b6.bind('<Button-1>',click)
b7 = Button(f1,text="=",font="lucida 25 bold",relief=SUNKEN,width=3,bg="blue",fg="white")
b7.pack(side="left",padx=5)
b7.bind('<Button-1>',click)
b8 = Button(f1,text="*",font="lucida 25 bold",relief=SUNKEN,width=3,bg="magenta")
b8.pack(side="left",padx=5)
b8.bind('<Button-1>',click)

f1 = Frame(root,bg="grey")
f1.pack(side="bottom",anchor ="n",padx=5 ,pady=5)

b5 = Button(f1,text="Del",font="lucida 25 bold",relief=SUNKEN,width=3,bg="black",fg="white")
b5.pack(side="left",padx=5)
b5.bind('<Button-1>',click)
b6 = Button(f1,text="AC",font="lucida 25 bold",relief=SUNKEN,width=3,bg="red",fg="white")
b6.pack(side="left",padx=5)
b6.bind('<Button-1>',click)
b7 = Button(f1,text="%",font="lucida 25 bold",relief=SUNKEN,width=3,bg="magenta")
b7.pack(side="left",padx=5)
b7.bind('<Button-1>',click)

root.mainloop()