#Tkinker = GUI(Graphical User Interface)
import tkinter

window = tkinter.Tk()
window.title("My window")
window.minsize(500, 300)

def button_clicked():
    print("I got clicked")
    my_label["text"] = input.get()

# 레이블 만들어보기
my_label = tkinter.Label(text="I'm a label", font=("Arial", 24, "bold"))
my_label.pack(side="top")
## 레이블을 완성하고 위치 조정을 해준다.
my_label["text"] = "New Text"

my_label.pack()
my_label.config(text="New_text 1")
#레이블 수정의 모습은 같다. 지정해주던가, 아니면 컨피그


button = tkinter.Button(text="Click me",command=button_clicked)
## 버튼에 리스너를 통해서 동작을 전달해준다.
button.pack()

# Entry : 텍스트 필드로서 인풋을 받는다.
input = tkinter.Entry(width=10)
input.pack()
#input.get()하면 텍스트필드 값을 가져오게 된다.
## 기타 위젯들 : text, spinbox, scle, checkbutton, radiobutton(샘플 참조)

window.mainloop()
# 윈도우가 계속해서 떠있게 해준다.


## 팅커 레이아웃 대표적 3개 : pack(), place(), grid()
'''
pack은 다함께 움직여서 좀 컨트롤이 어렵다
my_label.pack()

place는 정확하게 위치해야 할 곳을 좌표로 정해줄 수 있다.
my_label.place(x=100, y=100) : 다음과 같이 지정 가능하다. 픽셀단위로 지정해서 위치 시키는게 가능하다.
이 친구의 단점은 너무 정확하게 작용을 해줘야한다는 것이다.

grid는 매우 간단한 개념이다 : 그리드는 표처럼 생각하고 디자인을 하는 것이다.
my_label.grid(column=0, row=0)
button.grid(column=1, row=1)
이런식으로 칸 단위로 채우는 것이다.

그리드와 팩은 같이 쓸 수 없다.
같이 쓰면 못쓴다고 에러가 난다.

ㅁㅁㅁ
ㅁㅁㅁ
ㅁㅁㅁ

그리드는 이런식으로 레이아웃을 나눠서 생각하는 것이다.

마지막으로는 위젯간의 padding을 주는 것이다.

만약 모든 것에 원한다면
window.config(padx=00, pady=00) : 뷰 자체에 패딩을 준다. 그러면 외곽선에서 패딩이 생긴다.
button.config(padx=00, pady=00) : 엘리먼트 자체를 통제해준다.

'''




