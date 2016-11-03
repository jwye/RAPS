import sys
import serial
import time
from struct import *
import RPi.GPIO as GPIO

# open AMA0
print("Opening Serial Port...")
ser = serial.Serial(
    port ='/dev/ttyS0',
    baudrate = 9600,
    parity = serial.PARITY_NONE,
    stopbits = 1,
    bytesize = 8
    )
print("Done")

#print("SET PIN18 HIGH")
#pin = 18 #
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(pin, GPIO.OUT) #
#GPIO.output(pin, GPIO.HIGH) #
#GPIO.output(pin, GPIO.LOW) #
#print("Done")

print(ser)
# delay
#ser.flushInput()
print("Done")
def main():
    while True:
        # get from buffer
        count = ser.inWaiting()
        recv = ser.read(count)
        print(count)
        print(recv)
        ser.write([0x55])
        # delay
        time.sleep(0.1)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        if ser != None:
            ser.close()
