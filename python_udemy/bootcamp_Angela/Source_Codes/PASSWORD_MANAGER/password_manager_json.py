import json
from tkinter import *
from tkinter import messagebox
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generated():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    list_letters = [item for item in random.choices(letters, k=nr_letters)]
    list_symbols = [sym for sym in random.choices(symbols, k=nr_symbols)]
    list_numbers = [num for num in random.choices(numbers, k=nr_numbers)]
    # choices 함수(sequence, weights="", cumweights"", k= 갯수)

    password_list = list_letters + list_symbols + list_numbers
    password_list1 = "".join(password_list)
    field3.delete(0, END)
    field3.insert(0, password_list1)
    
    #generate버튼을 누르면 클립보드에 복사해보자. pyperclip 라이브러리를 이용한다.
    pyperclip.copy(password_list1)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    website = field1.get()
    email = field2.get()
    password = field3.get()
    
    new_data = {
        website: {
            "email" : email,
            "password" : password
        }
    }
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="Please make sure you haven't left any fields!")
    else:
        try:
            with open("/Users/kyungyunlee/Desktop/PYTHON/PYTHON_UDEMY/BOOTCAMP_ANGELA/SOURCE_CODES/PASSWORD_MANAGER/data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("/Users/kyungyunlee/Desktop/PYTHON/PYTHON_UDEMY/BOOTCAMP_ANGELA/SOURCE_CODES/PASSWORD_MANAGER/data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #updating data
            data.update(new_data)
            
            with open("/Users/kyungyunlee/Desktop/PYTHON/PYTHON_UDEMY/BOOTCAMP_ANGELA/SOURCE_CODES/PASSWORD_MANAGER/data.json", "w") as data_file:
                #saving data
                json.dump(data, data_file, indent=4)
        finally:
            field1.delete(0, END)
            field3.delete(0, END)
    
# ---------------------------- FIND DATA ------------------------------- #
def search():
    website = field1.get()
    
    try:
        with open("/Users/kyungyunlee/Desktop/PYTHON/PYTHON_UDEMY/BOOTCAMP_ANGELA/SOURCE_CODES/PASSWORD_MANAGER/data.json", "r") as data_file:
            #Reading old data
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Notification", message="There is no file yet")
    else:
        email = data[website]["email"]
        password = data[website]["password"]
        messagebox.showinfo(title="Notification", message=f"your password : {password}\nyour Email : {email}")
    
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
background_image = PhotoImage(file="/Users/kyungyunlee/Desktop/PYTHON/PYTHON_UDEMY/BOOTCAMP_ANGELA/SOURCE_CODES/PASSWORD_MANAGER/logo.png")
canvas.create_image(100, 100, image=background_image)
canvas.grid(column=1, row=0)

label1 = Label(text="Website :")
label1.grid(column=0, row=1)

field1 = Entry(width=35)
field1.grid(column=1, row=1)
field1.insert(0, "Amazon")

button0 = Button(text="Search", command=search)
button0.grid(column=2, row=1)


label2 = Label(text="Email and Username :")
label2.grid(column=0, row=2)

field2 = Entry(width=35)
field2.grid(column=1, row=2, columnspan=2)
field2.focus()
field2.insert(0, "leeky16498@gmail.com")
# 0, END는 커서의 앞뒤를 지정한다.

label3 = Label(text="Password :")
label3.grid(column=0, row=3)

field3 = Entry(width=21)
field3.grid(column=1, row=3)
field3.insert(0, "dlruddbs1!")

button1 = Button(text="Generate Password", command=password_generated)
button1.grid(column=2, row=3)

button2 = Button(text="ADD", command=save_data)
button2.grid(column=1, row=4, columnspan=2)
button2.config(width=36)

window.mainloop()