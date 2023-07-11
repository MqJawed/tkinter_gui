from tkinter import *
from PIL import Image, ImageTk

root = Tk() # Tk is a widget toolkit which has label button etc
root.title("h")

root.geometry("734x1255") # for size

# root.maxsize(734,434)
# root.minsize(734,434)
#l1 = Label(root,text = "Hello",)
#1.pack()

# for png files or gif files // spyder does'nt support png
#photo = PhotoImage(file = "spider.gif")

# for jpg file
    # when image and gui file not in same directory
#image = Image.open(r"C:\Users\MD QUZAL JAWED\Pictures\IMG0038A.jpg") 
    # when image and file in same directory
image2 = Image.open("Milad.jpg")
photo2 = ImageTk.PhotoImage(image2)


l2 = Label(image = photo2)
l2.pack()


root.mainloop()