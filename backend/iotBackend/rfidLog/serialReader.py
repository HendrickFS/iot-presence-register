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
    try:
        employee = employee.objects.get(rfid=employeeId)
        newLog = rfidLog(employee=employee)
        logs = rfidLog.objects.filter(employee=employee).order_by('-timestamp')
        if logs.count() == 0:
            newLog.type = 'IN'
        else:
            if logs[0].type == 'IN':
                newLog.type = 'OUT'
            else:
                newLog.type = 'IN'
        print("Employee: ", employee.name, " Type: ", newLog.type, " Time: ", newLog.timestamp)
        newLog.save()
    except:
        print("Employee not found")

def sensorsToSerial():
    from rfidLog.models import sensor
    ser = serial.Serial('COM4', 9600)
    print("Printing sensors states at serial port...")
    sensors = sensor.objects.all()
    for s in sensors:
        ser.write(s.id.encode())
        ser.write(b' ')
        ser.write(str(s.enabled).encode())
        ser.write(b'\n')

