#https://pyserial.readthedocs.io/en/latest/pyserial_api.html
import serial

# 시리얼 설정
ser = serial.Serial(port='COM6',
                    baudrate=115200,
                    parity='N',
                    stopbits=1,
                    bytesize=8,
                    timeout=8
                    )

#
ser.isOpen()

print(ser.name)

send_data = 'hello\r\n'

#데이터 쓰기
# bytearray 또는 memoryview 와 같은 바이트들로  전송
# 유니코드 문자열은 반드시 인코드(utf-8)
ser.write(send_data.encode('utf-8'))

# 입력 버퍼에 바이트 갯수를 얻기
print(ser.inWaiting())

while True:
    #한문자열 입력 대기
    input_data = ser.readline()
    # 10바이트 읽기
    #input_data = ser.read(10) 

    #바이트배열을 유니코드로 변환
    input_data = input_data.decode("utf-8")

    print(input_data)

