from tkinter import *
import requests

URL = "https://api.kanye.rest"

##--------Button Function------##
def click_button():
    global sentence
    request = requests.get(url=URL)
    request.raise_for_status()
    data = request.json()
    print(data)
    quote = data["quote"]
    canvas.itemconfig(canvas_text, text=quote)
    



##---------UI SETUP-----------##

window = Tk()
window.title("Kanye motivating Sentences")
window.config(padx=50, pady=50, bg="white")

title_label = Label(text="Kanye Request", font=("Arial", 50, "bold"), bg="white", fg="black", borderwidth=0, highlightthickness=0)
title_label.grid(column=1, row=0)

sentence = "This is the Kanye's motivation sentence!"
canvas = Canvas(width=400, height=400, bg="white", highlightthickness=0, borderwidth=0)
background_image = PhotoImage(file="/Users/kyungyunlee/Desktop/PYTHON/PYTHON_UDEMY/BOOTCAMP_ANGELA/SOURCE_CODES/KANYE_PROJECT/background.png")
canvas_image = canvas.create_image(200, 200, image=background_image)
canvas_text = canvas.create_text(200, 200, text=sentence, font=("Arial", 30, "bold"), width=190)
canvas.grid(column=1, row=1, pady=30)

button_background = PhotoImage(file="/Users/kyungyunlee/Desktop/PYTHON/PYTHON_UDEMY/BOOTCAMP_ANGELA/SOURCE_CODES/KANYE_PROJECT/kanye.png")
button = Button(image=button_background)
button.config(highlightthickness=0, bg="white", borderwidth=0, command=click_button)
button.grid(column=1, row=2)

window.mainloop()