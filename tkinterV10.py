from tkinter import * 
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk() # Créer une nouvelle fenêtre tkinter
root.title("Messages Boxes")
root.iconbitmap('C:/Users/Dev-Samuel/Documents/Python/Tkinter/tkinter/favicon.ico')

def popup():
    response = messagebox.askyesno("This is my Popup!", "Hello World!")
    #response = messagebox.showerror("This is my Popup!", "Hello World!")

    Label(root, text=response).pack()

Button(root, text="Popup", command=popup).pack()

root.mainloop()