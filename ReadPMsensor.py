#ref form http://watchword.space/blog/?p=26
#sudo vim /boot/cmdline.txt  del. console=serial0,115200 
#encoding=utf-8
import sys
import serial
import time
from struct import *
import RPi.GPIO as GPIO

# 打开串口
print("Opening Serial Port...")
ser = serial.Serial(
    port ='/dev/ttyAMA0',
    baudrate = 9600,
    parity = serial.PARITY_NONE,
    stopbits = serial.STOPBITS_ONE,
    bytesize = serial.EIGHTBITS,
    rtscts = 0,
    dsrdtr = 0,
    xonxoff =0
    )
print("Done")

print("SET PIN18 HIGH")
pin = 18 # 11管脚对于的BCM管脚号码
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT) #写
GPIO.output(pin, GPIO.HIGH) #工作
#GPIO.output(pin, GPIO.LOW) #休息
print("Done")
print(ser)

try:
    cnt = 0
    while True:
        # 获得接收缓冲区字符
        count = ser.inWaiting()
        if count >= 24:
            # 读取内容并回显
            recv = ser.read(count)
            cnt = cnt + 1
            print("[%d]Recieve Data" % cnt)
            print(len(recv), "Bytes:")
            tmp = recv[4:16]
            datas = unpack('>hhhhhh', tmp)
            print(datas)
            print("insert into pm_log ('pm1','pm2_5','pm10') values (%d,%d,%d)" % (datas[0], datas[1],datas[2]))
            #ser.write(recv)
            # 清空接收缓冲区
            ser.flushInput()
        # 必要的软件延时
        time.sleep(0.1)


except KeyboardInterrupt:
    if ser != None:
        ser.close()
