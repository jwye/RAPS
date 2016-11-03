#ref form http://watchword.space/blog/?p=26
#sudo vim /boot/cmdline.txt  del. console=serial0,115200
#encoding=utf-8
import sys
import serial
import time
from struct import *
import RPi.GPIO as GPIO

# open AMA0
print("Opening Serial Port...")
ser = serial.Serial(
    port ='/dev/serial0',
    baudrate = 9600,
    parity = serial.PARITY_NONE,
    stopbits = 1,
    bytesize = 8
    )
print("Done")

print("SET PIN18 HIGH")
pin = 18 #
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT) #
GPIO.output(pin, GPIO.HIGH) #
#GPIO.output(pin, GPIO.LOW) #
print("Done")
print(ser)

try:
    cnt = 0
    while True:
        # clear buffer
        print("flushInput")
        ser.flushInput()
        print("Done")

        # get from buffer
        print("inWaiting")
        count = ser.inWaiting()
        print("Done")
        if count >= 24:
            # read from buf
            recv = ser.read(count)
            cnt = cnt + 1
            print("[%d]Recieve Data" % cnt)
            print(len(recv), "Bytes:")
            tmp = recv[4:16]
            datas = unpack('>hhhhhh', tmp)
            print(datas)
            print("insert into pm_log ('pm1','pm2_5','pm10') values (%d,%d,%d)" % (datas[0], datas[1],datas[2]))
            #ser.write(recv)
            # clear buffer
            ser.flushInput()
        # delay
        time.sleep(0.1)


except KeyboardInterrupt:
    if ser != None:
        ser.close()
