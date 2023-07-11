from tkinter import *
from PIL import Image, ImageTk

root = Tk()

root.geometry("734x1255")

# root.maxsize(734,434)
# root.minsize(734,434)
# l1 = Label(text = "Hello",)
# l1.pack()

# for png files or gif files // spyder does'nt support png
#photo = PhotoImage(file = "spider.gif")

# for jpg file
    # when image and gui file not in same directory
#image = Image.open(r"C:\Users\MD QUZAL JAWED\Pictures\IMG0038A.jpg") 
    # when image and file in same directory
image = Image.open("IMG0038A.jpg")
photo = ImageTk.PhotoImage(image)


l2 = Label(image = photo)
l2.pack( )


root.mainloop()