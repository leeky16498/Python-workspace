#Tkinker = GUI(Graphical User Interface)
import tkinter

window = tkinter.Tk()
window.title("My window")
window.minsize(500, 300)

# 레이블 만들어보기
my_label = tkinter.Label(text="I'm a label", font=("Arial", 24, "bold"))
my_label.pack(side="top")
## 레이블을 완성하고 위치 조정을 해준다.
my_label["text"] = "New Text"

my_label.pack()
my_label.config(text="New_text 1")
#레이블 수정의 모습은 같다. 지정해주던가, 아니면 컨피그

def button_clicked():
    print("I got clicked")
    my_label["text"] = input.get()

button = tkinter.Button(text="Click me",command=button_clicked)
## 버튼에 리스너를 통해서 동작을 전달해준다.
button.pack()

# Entry : 텍스트 필드로서 인풋을 받는다.
input = tkinter.Entry(width=10)
input.pack()
#input.get()하면 텍스트필드 값을 가져오게 된다.
## 기타 위젯들 : text, spinbox, scle, checkbutton, radiobutton,

window.mainloop()
# 윈도우가 계속해서 떠있게 해준다.




