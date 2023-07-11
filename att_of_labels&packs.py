from tkinter import *

root = Tk()

root.geometry("444x245")
#Attributes of label
#text
#bd = background color 
#fd = foreground color
#font
    # = ("algerian",34, "bold")
    # = "algerian 34 bold
#padx 
#pady 
#borderstyling => relief => SUNKEN, RAISED, GROOVE RIDGE

#N.B: color should always be in string apart from it use either string or caps
# relief = SUNKEN or "sunken",,side = LEFT of "left"

l = Label(text = "Our  father who art\n\t Hallowed be thy name", bg = "green",
          fg = "white", font = "algerian 17 bold", padx = 5, pady = 25,
          borderwidth = 5,relief = RIDGE)
#Attributes of pack
#side = top, bottom , left right || bY default top
#anchor = nw, ne se, sw || to use sw, se change side to bottom
#fill
# padx
# pady

l.pack(side=BOTTOM, anchor = SW, padx=15,pady=56)

root.mainloop()