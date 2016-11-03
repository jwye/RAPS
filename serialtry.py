#! /usr/bin/python
import serial
import string
import time

# Raspberry Pi GPIO Serial Port settings
rpiCOM = '/dev/ttyAMA0'
baud = 9600
xtimes = 0
inbuff = 0

# Setup - if serial port can't be open an Exception will be raised
while True:
    try:
        ser = serial.Serial(rpiCOM, baud, timeout=1)
        # go out of while loop when connection is made
        break

    except serial.SerialException:
        print 'COM port ' + rpiCOM + ' not available. Wait...'
        time.sleep(3)

# Get input from serial buffer
while True:
    try:
        str = ""

        while 1:
           inbuff = ser.inWaiting()
           msgCOM = ser.read(inbuff)

           if msgCOM == '$OK':
                xtimes += 1
                print xtimes
                print "PIC Says: " + msgCOM
                print "inWaiting: %d" %inbuff
                ser.flushInput()
                inbuff = ser.inWaiting()
                print "Clear inbuff: %d" %inbuff
                break
           #str += msgCOM
    except serial.serialutil.SerialException:
        xtimnes = 0
        ser.close()
        time.sleep(3)
        ser = serial.Serial(rpiCOM, baud)
        ser.open()
        pass
