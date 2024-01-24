from tkinter import *
from PIL import ImageTk, Image
import sqlite3
from tkinter import messagebox

root = Tk()
root.title("Databases GUI")
root.iconbitmap('C:/Users/Dev-Samuel/Documents/Python/Tkinter/tkinter/favicon.ico')
root.geometry("400x400")
conn = sqlite3.connect('C:/Users/Dev-Samuel/Downloads/sqlite-tools-win-x64-3450000/menfou.db')
c = conn.cursor()

def query():
    conn = sqlite3.connect('C:/Users/Dev-Samuel/Downloads/sqlite-tools-win-x64-3450000/menfou.db')
    c = conn.cursor()

    c.execute("SELECT * FROM livres")
    records = c.fetchall()
    #print(records)

    print_records = ''
    for record in records:
        print_records += str(record) + "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=7, column=0, columnspan=2)

    conn.commit()
    conn.close()

def submit():
    conn = sqlite3.connect('C:/Users/Dev-Samuel/Downloads/sqlite-tools-win-x64-3450000/menfou.db')
    c = conn.cursor()
    c.execute("INSERT INTO livres VALUES (:id, :titre, :auteur, :annee_publication, :prix)",
            {
                'id': id.get(),
                'titre': titre.get(),
                'auteur': auteur.get(),
                'annee_publication': annee_publication.get(),
                'prix': prix.get()
            }  )

    conn.commit()
    conn.close()

    id.delete(0, END)
    titre.delete(0, END)
    auteur.delete(0, END)
    annee_publication.delete(0, END)
    prix.delete(0, END)

id = Entry(root, width=30)
id.grid(row=0, column=1, padx=20)
titre = Entry(root, width=30)
titre.grid(row=1, column=1)
auteur = Entry(root, width=30)
auteur.grid(row=2, column=1)
annee_publication = Entry(root, width=30)
annee_publication.grid(row=3, column=1)
prix = Entry(root, width=30)
prix.grid(row=4, column=1)

id_label = Label(root, text="ID")
id_label.grid(row=0, column=0)
titre_label = Label(root, text="Titre")
titre_label.grid(row=1, column=0)
auteur_label = Label(root, text="Auteur")
auteur_label.grid(row=2, column=0)
annee_publication_label = Label(root, text="Année de publication")
annee_publication_label.grid(row=3, column=0)
prix_label = Label(root, text="Prix")
prix_label.grid(row=4, column=0)

submit_btn = Button(root, text="Ajouter à la base de données", command=submit)
submit_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

query_btn = Button(root, text="Afficher les données", command=query)
query_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=137)


conn.commit()

conn.close()
root.mainloop()