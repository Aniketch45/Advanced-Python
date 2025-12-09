# import time                       #main Thread is non-Daemon to make a thread daemon it can be in inactive State
# from threading import *           #daemon thread is end when non daemon is end ex. gaming etc
# print("game started")
# def show():
#     for i in range(10,0,-1):
#         print(i)
#         time.sleep(1)

# t1=Thread(target=show)
# t1.daemon=True
# t1.start()
# time.sleep(6)
# print("Time Ended !")

import time
from threading import *
class Test():
    print("Enter number keys in 6 seconds")
    def test(self):
        num=[0]*9
        for i in range(9):
            a=int(input("->"))
            num[i]=a
            if num[i]<1 or num[i]>9:
                print("Wrong value Entered!")
        length=len(num)
        if length==9:
            print("all keys Pressed Successfully")
        else:
            print("Failed all keys not Pressed!")

c=Test()
th1=Thread(target=c.test)
th1.daemon=True
th1.start()
time.sleep(6)
print("Time Ended..")


#chatbox
            
