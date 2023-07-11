from tkinter import *
from tkinter import messagebox as tmsg

def about():
    print("We will help")
    a=tmsg.askquestion("What info you want","Want to know your Father")
    if a == "yes":
        tmsg.askokcancel("About Your father","I am your father")
    else:
       b=tmsg.askretrycancel("Vital info missing!","Your are gonna ignore a vital message")
       if b == "retry":
          return about()
        
def module():
    print("click to see module")

root = Tk()

main_menu = Menu(root)

s1 = Menu(main_menu)
s1.add_command(label="About",command=about)
s1.add_command(label = "Modules",command=module)
main_menu.add_cascade(label = "Help",menu = s1)

root.config(menu=main_menu)

#tmsg.askretrycancel("hello"," I will kill you")

root.mainloop()