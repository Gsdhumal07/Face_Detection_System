from tkinter import *
from PIL import Image, ImageTk



root_ganesh=Tk()
root_ganesh.geometry("1300x600")

image=Image.open(r"C:\Users\wn10\Desktop\face_recognisation_system\Camera Roll\background.jpg")
photo=ImageTk.PhotoImage(image)


ram_label=Label(image=photo)
ram_label.pack()

root_ganesh.mainloop()