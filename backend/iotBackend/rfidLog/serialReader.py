import serial
import threading

def readSerial():
    ser = serial.Serial('COM4', 9600)
    print("Listening serial port...")
    while True:
        print("Received: ", ser.readline())


def processData(data):
    print("Processing data: ", data)