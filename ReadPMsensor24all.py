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

def main():
    cnt = 0
    while True:
        # get from buffer
        count = ser.inWaiting()
        if count >= 24:
            # read from buf
            recv = ser.read(count)
            print(recv)
            cnt = cnt + 1
            print("[%d]Recieve Data" % cnt)
            print(len(recv), "Bytes:")
            tmp = recv[4:16]
            datas = unpack('>hhhhhh', tmp)
            print(datas)
            print("(pm1=%d,pm2_5=%d,pm10=%d)"\
             % (datas[0], datas[1],datas[2]))
            #ser.write(recv)
            tmp2 = recv
            datas2 = unpack('>hh\
            hhhhhhhhhh', tmp2)
            print(datas2)
            # clear buffer
            ser.flushInput()
            print("Done")

        # delay
        time.sleep(0.1)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        if ser != None:
            ser.close()
