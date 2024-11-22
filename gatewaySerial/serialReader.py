import serial
from api import *

def readSerial():
    ser = serial.Serial('COM4', 9600)
    print("Listening serial port...")
    while True:
        print(ser.readline())
        processData(ser.readline())

def processData(data):
    print("Processing data: ", data)
    data = data.decode("utf-8").replace("\r\n", "")
    data = data.split("-")
    sensorId = data[0]
    rfid = data[1]
    postLog(sensorId, rfid)