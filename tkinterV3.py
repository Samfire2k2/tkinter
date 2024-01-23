from tkinter import * 

root = Tk() # Créer une nouvelle fenêtre tkinter

def monClic():
    monLabel = Label(root, text="J'ai cliqué sur le bouton")
    monLabel.pack()

monBouton =  Button(root, text="Cliquez-moi", command=monClic, fg="blue", bg="red")
monBouton.pack()
root.mainloop()