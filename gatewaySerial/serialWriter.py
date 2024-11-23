import serial
from api import *
import time

def writeSerial():
    ser = serial.Serial('COM5', 9600)
    sensors = getSensors()
    states = {}
    for sensor in sensors:
        states[sensor["id"]] = sensor["state"]
    while True:
        newSensors = getSensors()
        for newSensor in newSensors:
            if states[newSensor["id"]] != newSensor["state"]:
                ser.write(f"{newSensor['id']}-{newSensor['state']}\n".encode())
                states[newSensor["id"]] = newSensor["state"]
        time.sleep(1)
    