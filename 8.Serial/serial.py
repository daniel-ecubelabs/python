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

#데이터 쓰기, 문자열은 유니코드, 장치에 전달할 때는 바이트로 변환 필요
ser.write(send_data.encode('utf-8'))

ser.inWaiting()

while True:
    #한문자열 입력 대기
    input_data = ser.readline()
    # 10바이트 읽기
    #input_data = ser.read(10) 

    #바이트배열을 유니코드로 변환
    input_data = input_data.decode("utf-8")

    print(input_data)

