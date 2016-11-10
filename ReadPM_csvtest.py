## -*- coding: utf-8 -*-
#ref form http://watchword.space/blog/?p=26
#

import sys
import serial
import time
from struct import *
import csv
# delay
#ser.flushInput()

# make rec file
recname=time.strftime("PMrec_%Y-%m-%d_%H:%M:%S", time.localtime())
print(recname)
f = open('pmdata/'+recname+'.csv', 'w', encoding = 'UTF-8')
f.write('time,pm1,pm2.5,pm10,fullserwords\n')

time.sleep(1)

for x in range(3):
    recrtime=time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime())
    f.write(recrtime+",%d,%d,%d\n"% (5,100,2319))
    time.sleep(1)
    
f.close()
print("Done1")


f = open('pmdata/'+recname+'.csv', 'r')
for row in csv.DictReader(f,['t','1','2','10']):
    print(row['2'])
    
print("Done2")

f = open('pmdata/'+recname+'.csv', 'r')
for row in csv.DictReader(f):
    print(row['time']+' pm2.5='+row['pm2.5'])

print("Done3")


f.close()
