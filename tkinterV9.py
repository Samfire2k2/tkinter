from tkinter import * 
from PIL import ImageTk, Image

root = Tk() # Créer une nouvelle fenêtre tkinter
root.title("Boutons Radios & Pizzas")
root.iconbitmap('C:/Users/Dev-Samuel/Documents/Python/Tkinter/tkinter/favicon.ico')

MODES = [("Pepperoni", "Pepperoni"),
         ("Cheese", "Cheese"),
         ("Mushroom", "Mushroom"),
         ("Onion", "Onion")]

pizza = StringVar()

for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)

def clicked(value):
    my_Label = Label(root, text=value)
    my_Label.pack()

myLabel = Label(root, text=pizza.get())
myLabel.pack()

myButton = Button(root, text="Click Me!", command=lambda: clicked(pizza.get()))
myButton.pack()
root.mainloop()