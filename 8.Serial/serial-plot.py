'''
serialdata 클래스의 모습이다. plot_data 메소드는 그래프를 출력하기 위해 코드를 조금만 변경했으므로 serial_run 메소드만 알면 이해하기 쉽다.
10~19번째 줄은 처음 serialdata객체를 초기화할때 원하는 COM Port가 연결돼있지 않다면 연결될 때까지 while문이 작동한다.
serial_run 메소드는 실제 데이터를 받는 부분이다. 이때 try 문에서 예외처리를 하는데 여기서 연결이 끊겼는지 확인한다.
29번째 줄은 self.ser.readline() 때문에 설정했다. 테스트에 사용한 값들의 마지막 값은 \n\n\r의 형태인데 readline()의 경우 마지막 \n \n \r[data] 의 형태로 읽게 되는데 필요 없는 값이 들어가 한번 넘어가기 위해 넣어준 코드이다.
48번째 줄의 코드는 포트가 다시 연결됐을때 자동적으로 연결하게 해주는 코드이다.
대부분의 코드가 테스트용으로 사용한 값들에 맞춰있어 조금 바꿔야 한다.
https://ddtxrx.tistory.com/entry/Python-Serial-Communication
'''	

class serialdata:
    def __init__(self, port, baudrate):
        self.port=port
        self.baudrate=baudrate
        self.counter=0
        self.connection=False
        self.exitThread=False
 
 
        while True:
            try:
                self.ser=serial.Serial(self.port,baudrate=self.baudrate)
 
            except serial.SerialException:
                continue
            else:
                print("connect",self.ser)
                self.connection=True
                break
 
    def serial_run(self):
        while True:
            if self.connection:
                
                try:
                    res=self.ser.readline()
                    data=res.decode('utf-8')
 
                    if data=='\r' or data=='\n':
                        continue
                    else:
                        self.counter+=1
                        self.datalist=data.split('\t')
                        for val in self.datalist:
                            print(float(val))
 
 
                except ValueError:
                    print("valueError")
                except serial.SerialException:
                    print("disconnect")
                    self.ser.close()
                    self.connection=False
                except UnicodeDecodeError:
                    print("UnicodeDecodeError")
                    
 
            else:
                while True:
                    try:
                        self.ser=serial.Serial(self.port,baudrate=self.baudrate)
 
                    except serial.SerialException:
                        continue
                    else:
                        print("connect",self.ser)
                        self.connection=True
                        break
    