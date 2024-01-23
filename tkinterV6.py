from tkinter import * 
from PIL import ImageTk, Image

root = Tk() # Créer une nouvelle fenêtre tkinter
root.title("Icons, Images & Exit Buttons")
root.iconbitmap('C:/Users/Dev-Samuel/Documents/Python/Tkinter/tkinter/favicon.ico')

my_img = ImageTk.PhotoImage(Image.open("C:/Users/Dev-Samuel/Documents/Python/Tkinter/tkinter/favicon.ico"))
my_Label = Label(image=my_img)
my_Label.pack()

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()