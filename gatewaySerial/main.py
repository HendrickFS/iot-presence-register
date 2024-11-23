from serialReader import readSerial
from serialWriter import writeSerial
from api import *
import serial
from threading import Thread

def main():
    Thread(target=readSerial, daemon=True).start()
    # Thread(target=writeSerial, daemon=True).start()
    while True:
        pass

main()