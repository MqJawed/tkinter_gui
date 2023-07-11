from tkinter import *

class GUI(Tk): # argument = Tk; to use default classes as label,button etc
     def __init__(self):
        super().__init__()
        self.geometry("777x555")
     def createbutton(self, inptext):
            Button(text=inptext,command=self.destroy).pack()
       

if __name__ == '__main__':
    window = GUI() # creating object window of gui class
    window.createbutton("click")
    window.mainloop()
    

# this is one of the way to create gui when dealing with lot of new guiss