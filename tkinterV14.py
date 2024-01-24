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
editor = Toplevel()

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

def delete():
    conn = sqlite3.connect('C:/Users/Dev-Samuel/Downloads/sqlite-tools-win-x64-3450000/menfou.db')
    c = conn.cursor()
    c.execute("DELETE from livres WHERE oid= " + delete_box.get())
    delete_box.delete(0, END)

    conn.commit()
    conn.close()

def update():
    conn = sqlite3.connect('C:/Users/Dev-Samuel/Downloads/sqlite-tools-win-x64-3450000/menfou.db')
    c = conn.cursor()

    id_editor = delete_box.get()
    c.execute("""UPDATE livres SET
        titre = :titre,
        auteur = :auteur,
        annee_publication = :annee_publication,
        prix = :prix

        WHERE oid = :oid""",
        {
            'titre': titre_editor.get(),
            'auteur': auteur_editor.get(),
            'annee_publication': annee_publication_editor.get(),
            'prix': prix_editor.get(),
            'oid': id_editor.get()
        })


    conn.commit()
    conn.close()
    editor.destroy()
    root.deiconify()

def edit():
    root.withdraw()
    global editor
    editor = Tk()
    editor.title("Modifier une entrée")
    editor.iconbitmap('C:/Users/Dev-Samuel/Documents/Python/Tkinter/tkinter/favicon.ico')
    editor.geometry("400x400")
    conn = sqlite3.connect('C:/Users/Dev-Samuel/Downloads/sqlite-tools-win-x64-3450000/menfou.db')
    c = conn.cursor()
    record_id = clicked.get()

    c.execute("SELECT * FROM livres")
    records = c.fetchall()

    global id_editor
    global titre_editor
    global auteur_editor
    global annee_publication_editor
    global prix_editor

    id_editor = Entry(editor, width=30)
    id_editor.grid(row=0, column=1, padx=20)
    titre_editor = Entry(editor, width=30)
    titre_editor.grid(row=1, column=1)
    auteur_editor = Entry(editor, width=30)
    auteur_editor.grid(row=2, column=1)
    annee_publication_editor = Entry(editor, width=30)
    annee_publication_editor.grid(row=3, column=1)
    prix_editor = Entry(editor, width=30)
    prix_editor.grid(row=4, column=1)

    id_label = Label(editor, text="ID")
    id_label.grid(row=0, column=0)
    titre_label = Label(editor, text="Titre")
    titre_label.grid(row=1, column=0)
    auteur_label = Label(editor, text="Auteur")
    auteur_label.grid(row=2, column=0)
    annee_publication_label = Label(editor, text="Année de publication")
    annee_publication_label.grid(row=3, column=0)
    prix_label = Label(editor, text="Prix")
    prix_label.grid(row=4, column=0)


    print_records = ''
    for record in records:
        print_records += str(record) + "\n"

    edit_btn = Button(editor, text="Modifier les données", command=update)
    edit_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=143)


def show_id():
	# Create a database or connect to one
	conn = sqlite3.connect('C:/Users/Dev-Samuel/Downloads/sqlite-tools-win-x64-3450000/menfou.db')
	# Create cursor
	c = conn.cursor()

	# Query the database
	c.execute("SELECT oid FROM livres")
	records = c.fetchall()
	# print(records)

	options = []
	global clicked 
	clicked = StringVar()
	

	# Loop Thru Results
	print_records = ''
	for record in records:
		options.append(str(record[0]))

	clicked.set(options[0])
	drop = OptionMenu(root, clicked, *options)
	drop.grid(row=20, column=0, columnspan=2)

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

delete_box = Entry(root, width=30)
delete_box.grid(row=8, column=1, pady=5)

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

delete_box_label = Label(root, text="ID à supprimer")
delete_box_label.grid(row=8, column=0, pady=5)

submit_btn = Button(root, text="Ajouter à la base de données", command=submit)
submit_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

query_btn = Button(root, text="Afficher les données", command=query)
query_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

delete_btn = Button(root, text="Supprimer les données", command=delete)
delete_btn.grid(row=9, column=0, columnspan=2, pady=10, padx=10, ipadx=136)

edit_btn = Button(root, text="Mettre à jour l'enregistrement", command=edit)
edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=143)

conn.commit()

conn.close()
root.mainloop()