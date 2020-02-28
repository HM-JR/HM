'''
    间隔两秒显示时间
'''
import  time
count=0
b=open("timefile","a+")
b.seek(0, 0)
item = b.readlines()
if  len(item):
    count = len(item)
while True:
    count+=1
    b.write(str(count) +"."+str(time.ctime())+"\n")
    b.flush()
    time.sleep(2)

