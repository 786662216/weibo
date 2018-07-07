#coding:utf-8
import os
import time
import datetime
while True:
    a = os.popen('ps -ef|grep ssserver|grep -v grep').read()#获取执行命令的结果，OS.SYSTEM是执行并打印执行结果，返回值是其他东西
    print a + str(datetime.datetime.now())
    if 'ssserver' in a:
        print 'do nothing' + str(datetime.datetime.now())
    else:
        os.system('ssserver -p 8000 -k password -m rc4-md5 -d start')
    time.sleep(1000)
#nohup python -u ssguardian.py > ss.log &
