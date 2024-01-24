from tkinter import *
from PIL import ImageTk, Image
import sqlite3
from tkinter import messagebox

root = Tk()
root.title("Databases")
root.iconbitmap('C:/Users/Dev-Samuel/Documents/Python/Tkinter/tkinter/favicon.ico')
root.geometry("400x400")

try:
    conn = sqlite3.connect('C:/Users/Dev-Samuel/Downloads/sqlite-tools-win-x64-3450000/menfou.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE livres (
    id INTEGER PRIMARY KEY,
    titre TEXT,
    auteur TEXT,
    annee_publication INTEGER,
    prix REAL
);
""")
    conn.commit()
    messagebox.showinfo("Connecté à la base SQLite !")
except sqlite3.Error as error:
    messagebox.showerror("ERREUR", f"Une erreur est survenue: {error}")
finally:
    if conn:
        conn.close()

root.mainloop()