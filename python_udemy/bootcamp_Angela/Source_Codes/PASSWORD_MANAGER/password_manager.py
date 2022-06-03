from tkinter import *
from tkinter import messagebox
import random
import pyperclip

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
    # messagebox.showinfo(title="Alerts",message="Your information is added well.")
    
    if len(field1.get()) == 0 or len(field2.get()) == 0 or len(field3.get()) == 0:
        messagebox.showwarning(title="Warning", message="There is some empty information, Check it please.")
    else:
        is_ok = messagebox.askokcancel(title=field1.get(), message= f"Theses are your details you entered:\nEmail : {field2.get()}\nPassword : {field3.get()}\n Is everything OK to save?")
    
        if is_ok:
            with open("/Users/kyungyunlee/Desktop/PYTHON/PYTHON_UDEMY/BOOTCAMP_ANGELA/SOURCE_CODES/PASSWORD_MANAGER/data.txt", "a") as data:
                data.write("{0} | {1} | {2}\n".format(field1.get(), field2.get(), field3.get()))
                field1.delete(0, END)
                field2.delete(0, END)
                field3.delete(0, END) 
            
    
    

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
background_image = PhotoImage(file="BOOTCAMP_ANGELA/SOURCE_CODES/PASSWORD_MANAGER/logo.png")
canvas.create_image(100, 100, image=background_image)
canvas.grid(column=1, row=0)

label1 = Label(text="Website :")
label1.grid(column=0, row=1)

field1 = Entry(width=35)
field1.grid(column=1, row=1, columnspan=2)
field1.insert(0, "Amazon")


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