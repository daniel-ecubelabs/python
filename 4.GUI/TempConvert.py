from tkinter import *
from convert import *

#3.1 GUI를 구현할 때는 클래스로 윈도우를 나타내는 것이 보통
class App:
    #3.2 클래스의 새로운 인스턴스가 만들어질 때 사용되는 메서드(일종의 생성자)
    def __init__(self, master):
        #3.3 프레임 객체는 애플리케이션 윈도우를 구성하게 될 라벨과 그 밖의 항목을 담는다.
        frame = Frame(master)
        
        #3.4 프레임의 pack 메서드(사용가능한 공간에 감싸 안으라고 알린다.)
        frame.pack()
        
        #3.5 라벨을 추가할 때 grid 메서드 사용하면 레이아웃을 사용자 인터페이스에 지정할 수 있다.
        #필드의 시작 위치는 그리드의 0,0이고 행과 열로 지정 가능
        Label(frame, text='deg C').grid(row=0, column=0)
        
        #3.6 특별한 변수 객체의 인스턴스를 만들어야 한다.가장 흔하게 사용되는 것은 StringVar
        #숫자를 입력하고 표시할 것이기 때문에 여기서는 DoubleVar사용한다. 
        #DoubleVar는 배정밀도 부동소수점수를 가리키며, float 비슷하지만 훨씬 더 정확한 타입
        self.c_var = DoubleVar()
        
        #3.7 c_var는 textvariable 속성 지정되어 엔트리로 대입된다.
        #이 엔트리가 DoubleVar에 담긴 것을 표시하고, 값이 변경되면 자동으로 업데이트된다.
        Entry(frame, textvariable=self.c_var).grid(row=0, column=1)
        
        #3.8 다음 행에 라벨 추가 
        Label(frame, text='deg F').grid(row=1, column=0)
        
        #3.9 온도 변환 계산 결과를 표시하는 변수 인스턴스 생성
        self.result_var = DoubleVar()
        
        #3.10 result_var는 textvariable 속성을 가지고 라벨로 대입된다. 
        Label(frame, textvariable=self.result_var).grid(row=1,column=1)
        
        #3.11 convert 버튼을 클릭하면 변환 값을 볼 수 있는 버튼을 생성한다.
        #버튼 클래스에서 convert 메서드를 호출하도록 지정
        
        button = Button(frame, text='Convert', command=self.convert)
        
        #3.12 그리드 메서드의 columnspan=2 지정하여 양 옆으로 충분한 여백을 지정
        button.grid(row=2, columnspan=2)
        
        #3.13 생성자에서 변환기 한 번만 만들고 버튼을 클릭될 때마다 동일한 변환기를 사용하도록
        #self.t_conv 라는 변수를 만들어 변환기를 참조하기로 한다. 
        self.t_conv = ScaleAndOffsetConvert('C', 'F', 1.8, 32)
        
    #3.14 App 클래스의 convert 메서드
    def convert(self):
        c = self.c_var.get()
        self.result_var.set(self.t_conv.convert(c))


#1. Tk()객체를 root 변수에 지정
root = Tk()
#2. 애플리케이션 윈도우 제목은 Temp Converter 라벨 생성 
root.wm_title('Temp Converter')
#3. App 클래스에 Tk 루트 객체를 넘기고 app 인스턴스를 생성
app = App(root)
#4. 루트 인스턴스를 계속 실행
root.mainloop()

