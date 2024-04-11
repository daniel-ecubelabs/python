#https://pyserial.readthedocs.io/en/latest/pyserial_api.html
import serial

# 시리얼 설정
ser = serial.Serial(port='COM11',
                    baudrate=115200,
                    parity='N',
                    stopbits=1,
                    bytesize=8,
                    timeout=3
                    )

#
ser.isOpen()

print(ser.name)

send_data = 'AT\r\n'


ser.reset_input_buffer()

#데이터 쓰기
# bytearray 또는 memoryview 와 같은 바이트들로  전송
# 유니코드 문자열은 반드시 인코드(utf-8)
ser.write(send_data.encode('utf-8'))

#input_data = ser.readline()
#input_data = ser.read(10)

input_data = b''

print(ser.inWaiting())
input_data += ser.read(10)
      
print(input_data.decode('utf-8'))
