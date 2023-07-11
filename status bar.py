from tkinter import *

def download():
    status.set("Downloading...")
    status.update()
    import time
    time.sleep(2)
    status.set("Downloaded")
    
root = Tk()
root.geometry("777x444")

status=StringVar()
status.set("READY")
l1 = Label(textvariable=status,font="lucida 9 ",anchor="w",relief=RIDGE)
l1.pack(side=BOTTOM,fill=X)

Button(text="Download",font = "Helvetica 12 bold",padx=8,pady=8,command=download).pack(pady=80)
root.mainloop()