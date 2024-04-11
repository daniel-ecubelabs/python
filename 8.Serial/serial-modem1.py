#https://pyserial.readthedocs.io/en/latest/pyserial_api.html
import serial
import time

ATCmdList = {
    'IMEI': {'CMD': "AT+CGSN", 'REV': "\r\nOK\r\n"},
    'FWInfo': {'CMD': "AT+CGMR", 'REV': "\r\nOK\r\n"},
    'HWInfo': {'CMD': "AT+CGMM", 'REV': "\r\nOK\r\n"},
}

class MODEM:
    ser = None
    def __init__(self, port='COM11', baudrate=115200):
        self.port=port
        self.baudrate=baudrate

        self.ser = serial.Serial(self.port,
                                 self.baudrate,
                                 parity='N',
                                 stopbits=1,
                                 bytesize=8,
                                 timeout=5
                                 )
        self.compose = ""
        self.response = ""
        self.timeout = 5
        self.ser.isOpen()
        print(self.ser.name)

    def sendATCmd_(self, command):
        #print('sendATCmd_'+ str(command))
        self.compose = ""
        self.compose = str(command) + "\r\n"
        self.ser.reset_input_buffer()
        self.ser.write(self.compose.encode('utf-8'))

    def __getMillSec(self):
        ''' get miliseconds '''
        return int(time.time())

    def __delay(self, ms):
        ''' delay as millseconds '''
        time.sleep(float(ms/1000.0))
        
    def __readATResponse(self, cmd_response):
        ''' getting respnse of AT command from modem '''
        timer = self.__getMillSec()
        timeout = self.timeout
        response = self.response

        while True:
            self.response = ""
            while(self.ser.inWaiting()):
                try:
                    self.response = self.ser.read(self.ser.inWaiting()).decode('utf-8', errors='ignore')
                    #print("read response: " + self.response)
                    response = self.response
                    self.__delay(50)
                except Exception as e:
                    print(e)
                    return False
            if(self.response.find(cmd_response) != -1):
                #print("read response: " + self.response)
                return True
            if((self.__getMillSec() - timer) > timeout):
                # error rasie
                print("Recv failed: " + response)
                return False
        
    def sendATCmd(self, command, cmd_response, timeout = None):
        ''' Send AT command & Read command response '''
        #print('sendATCmd')
        if(self.ser.isOpen() == False):
            print("ser.isOpen false")
            self.ser.open()

        if timeout is None:
            timeout = self.timeout
            
        self.sendATCmd_(command)

        timer = self.__getMillSec()

        while True: 
            if((self.__getMillSec() - timer) > timeout):
                # error rasie
                print(command + " / Send failed ")
                return "Error"
            
            if(self.__readATResponse(cmd_response)):
                return self.response

    # AT command methods
    def getIMEI(self):
        ''' get IMEI number'''
        data = self.sendATCmd(ATCmdList['IMEI']['CMD'], ATCmdList['IMEI']['REV'])
        return data[:data.index(ATCmdList['IMEI']['REV'])]

    def getFirmwareInfo(self):
        ''' get FW version '''
        data =  self.sendATCmd(ATCmdList['FWInfo']['CMD'], ATCmdList['FWInfo']['REV'])
        return data[:data.index(ATCmdList['FWInfo']['REV'])]

if __name__ == '__main__':
    print("main")
    node = MODEM()

    print("AT: " + node.sendATCmd("AT", "OK\r\n"))
    print("IMEI: " + node.getIMEI())
    print("FW Ver: " + node.getFirmwareInfo())
    #print("HW model: " + node.getHardwareInfo())
    #print("Phone Number: " + node.getPhoneNumberInfo())

    time.sleep(2)
