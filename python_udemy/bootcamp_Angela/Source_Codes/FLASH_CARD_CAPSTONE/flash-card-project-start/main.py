import pandas as pd
from tkinter import *
from turtle import right
import time
import random
#--------------- Get data from CSV ---------------#

try:  
    data = pd.read_csv("/Users/kyungyunlee/Desktop/PYTHON/PYTHON_UDEMY/BOOTCAMP_ANGELA/SOURCE_CODES/FLASH_CARD_CAPSTONE/flash-card-project-start/data/word_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("/Users/kyungyunlee/Desktop/PYTHON/PYTHON_UDEMY/BOOTCAMP_ANGELA/SOURCE_CODES/FLASH_CARD_CAPSTONE/flash-card-project-start/data/french_words.csv")    
finally:
    to_learn = data.to_dict(orient="records")
current_card = {}

print(to_learn)
##판다스에서 데이터 다루는 것 한번 정확하게 찾아보면 도움이 많이 될 듯 하다.

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=front_image)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=back_image)

def is_known():
    to_learn.remove(current_card) ## 지정된 딕셔너리 자체를 직접 지우는게 가능하다.
    
    data = pd.DataFrame(to_learn)
    data.to_csv("/Users/kyungyunlee/Desktop/PYTHON/PYTHON_UDEMY/BOOTCAMP_ANGELA/SOURCE_CODES/FLASH_CARD_CAPSTONE/flash-card-project-start/data/word_to_learn.csv")
    
    
    next_card()

    
## French : English 딕셔너리 작성 완료.

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash cards")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
back_image = PhotoImage(file="/Users/kyungyunlee/Desktop/PYTHON/PYTHON_UDEMY/BOOTCAMP_ANGELA/SOURCE_CODES/FLASH_CARD_CAPSTONE/flash-card-project-start/images/card_back.png")
front_image = PhotoImage(file="/Users/kyungyunlee/Desktop/PYTHON/PYTHON_UDEMY/BOOTCAMP_ANGELA/SOURCE_CODES/FLASH_CARD_CAPSTONE/flash-card-project-start/images/card_front.png")
card_background = canvas.create_image(400, 263, image=front_image)
card_title = canvas.create_text(400, 150, text="French", fill="black", font=("Arial", 45, "italic"))
card_word = canvas.create_text(400, 263, text="Meaning", fill="black", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=5)

right_image = PhotoImage(file="/Users/kyungyunlee/Desktop/PYTHON/PYTHON_UDEMY/BOOTCAMP_ANGELA/SOURCE_CODES/FLASH_CARD_CAPSTONE/flash-card-project-start/images/right.png")
button1 = Button(image=right_image, highlightthickness=0, borderwidth=0, command=next_card)
button1.grid(column=1, row=1)

wrong_image = PhotoImage(file="/Users/kyungyunlee/Desktop/PYTHON/PYTHON_UDEMY/BOOTCAMP_ANGELA/SOURCE_CODES/FLASH_CARD_CAPSTONE/flash-card-project-start/images/wrong.png")
button2 = Button(image=wrong_image, highlightthickness=0, borderwidth=0, command=is_known)
button2.grid(column=3, row=1)

next_card()

window.mainloop()


    