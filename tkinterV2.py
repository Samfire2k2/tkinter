from tkinter import * 

root = Tk() # Créer une nouvelle fenêtre tkinter
monLabel1 = Label(root, text="Hello World")
monLabel2 = Label(root, text="Je suis une étiquette")
monLabel1.grid(row=0, column=0)
monLabel2.grid(row=1, column=0)
root.mainloop()