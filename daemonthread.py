import time                       #main Thread is non-Daemon thread to make thread daemon it can be inactive 
from threading import *           #daemon thread is end when non daemon is end used in gaming
print("game started")
def show():
    for i in range(10,0,-1):
        print(i)
        time.sleep(1)

t1=Thread(target=show)
t1.daemon=True
t1.start()
time.sleep(6)
print("Time Ended !")