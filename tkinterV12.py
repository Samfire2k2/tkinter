from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Dropdown Menus")
root.iconbitmap('C:/Users/Dev-Samuel/Documents/Python/Tkinter/tkinter/favicon.ico')
root.geometry("400x400")

def show():
    myLabel = Label(root, text=clicked.get()).pack()

clicked = StringVar()
clicked.set("Monday")

drop = OptionMenu(root, clicked, "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
drop.pack()

myButton = Button(root, text="Show Selection", command=show).pack()

root.mainloop()