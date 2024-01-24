from tkinter import * 
from PIL import ImageTk, Image

root = Tk() # Créer une nouvelle fenêtre tkinter
root.title("Icons, Images & Exit Buttons")
root.iconbitmap('C:/Users/Dev-Samuel/Documents/Python/Tkinter/tkinter/favicon.ico')

my_img1 = ImageTk.PhotoImage(Image.open("C:/Users/Dev-Samuel/Documents/Python/Tkinter/tkinter/favicon.ico"))
my_img2 = ImageTk.PhotoImage(Image.open("C:/Users/Dev-Samuel/Documents/Python/Tkinter/tkinter/image1.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("C:/Users/Dev-Samuel/Documents/Python/Tkinter/tkinter/image2.jpg"))
image_list = [my_img1, my_img2, my_img3]


my_Label = Label(image=my_img1)
my_Label.grid(row=0, column=0, columnspan=3)

def forward(image_number):
    global my_Label
    global button_forward
    global button_back

    if image_number > len(image_list): 
        return 

    my_Label.grid_forget()
    my_Label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1), state=DISABLED)
    my_Label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    status = Label(root, text="Image "+ str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=2, columnspan=3)
    
    if image_number == len(image_list):
        button_forward = Button(root, text=">>", state=DISABLED)
        
def back(image_number):
    global my_Label
    global button_forward
    global button_back

    my_Label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))
    my_Label.grid(row=0, column=0, columnspan=3)

    if image_number == 0:
        button_back = Button(root, text="<<", state=DISABLED)

    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

button_back = Button(root, text="<<", command=back)
button_exit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()