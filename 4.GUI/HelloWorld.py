from tkinter import *
#1. Tk객체를 root 변수에 지정
root = Tk()
#2. Label 클래스의 인스턴스를 생성하고, root 변수를 첫 번째 인수로 입력한다.
#두 번째 인수는 라벨에 표시할 텍스트가 지정하고, pack메서드가 호출된다.
#pack 메서드는 사용 가능한 공간에 맞춰 감싸 안으라고 알리는 것이다.
Label(root, text='Hello World').pack()
#3. 
root.mainloop()
