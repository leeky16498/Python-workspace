# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
background_image = PhotoImage(file="BOOTCAMP_ANGELA/SOURCE_CODES/PASSWORD_MANAGER/logo.png")
canvas.create_image(100, 100, image=background_image)
canvas.grid(column=1, row=0)

label1 = Label(text="Website :")
label1.grid(column=0, row=1)

label2 = Label(text="Email and Username :")
label2.grid(column=0, row=2)

label3 = Label(text="Password :")
label3.grid(column=0, row=3)


window.mainloop()