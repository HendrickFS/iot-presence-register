import serial
from api import *
from serialWriter import writeSerial

def readSerial():
    ser = serial.Serial('COM5', 9600)
    print("Listening serial port...")
    while True:
        try:
            data = ser.readline()
            print(data)
            processData(data)
        except Exception as e:
            print(e)

def processData(data):
    print("Processing data: ", data)
    data = data.decode("utf-8").replace("\r\n", "")
    sensorId = data[0:2]
    rfid = data[2:10]
    postLog(sensorId, rfid)