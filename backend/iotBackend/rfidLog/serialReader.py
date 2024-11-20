import serial
import threading

def readSerial():
    ser = serial.Serial('COM4', 9600)
    print("Listening serial port...")
    while True:
        print("Received: ", ser.readline())
        processData(ser.readline())


def processData(data):
    from rfidLog.models import employee, rfidLog
    employeeId = data.decode('utf-8')
    employeeId = employeeId.replace('\r\n', '')
    employee = employee.objects.get(rfid=employeeId)
    print("Employee: ", employee)
    employee.save()