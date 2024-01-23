from tkinter import * 

root = Tk() # Créer une nouvelle fenêtre tkinter

e = Entry(root, width=50)
e.pack()
e.insert(0, "Entrez votre nom: ") ##s'ajoute à la chaîne de caractère

def monClic():
    hello = "Hello " + e.get()
    monLabel = Label(root, text=hello)
    monLabel.pack()

monBouton =  Button(root, text="Cliquez-moi", command=monClic, fg="white", bg="black")
monBouton.pack()
root.mainloop()