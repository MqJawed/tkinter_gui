from tkinter import *

root = Tk()
def hello():
    pass

# main_menu = Menu(root)
# main_menu.add_command(label="File",command=hello);
# main_menu.config(menu=new_menu)

main_menu = Menu(root)

submenu1 = Menu(main_menu,tearoff=0) # to disable tear of submenu 
submenu1.add_command(label = "New file",command= hello)
submenu1.add_command(label = "Save",command= hello)
submenu1.add_command(label = "Save as",command= hello)
submenu1.add_separator() # to draw a separator line
submenu1.add_command(label = "Open",command= hello)
submenu1.add_command(label = "Open as",command= hello)
main_menu.add_cascade(label = "File",menu = submenu1) # packing the submenus in a single label

submenu2 = Menu(main_menu) # tear off enable
submenu2.add_command(label = "New file",command= hello)
submenu2.add_command(label = "Save",command= hello)
submenu2.add_command(label = "Save as",command= hello)
submenu2.add_separator() # to draw a separator line
submenu2.add_command(label = "Open",command= hello)
submenu2.add_command(label = "Open as",command= hello)
main_menu.add_cascade(label = "Edit",menu = submenu2)

root.config(menu = main_menu)

root.mainloop()

