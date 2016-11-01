#ref form http://watchword.space/blog/?p=26
#encoding=utf-8
import serial
import time
from struct import *

# 打开串口
print("Opening Serial Port...")
ser = serial.Serial("/dev/ttyAMA0", 9600)
print("Done")
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
