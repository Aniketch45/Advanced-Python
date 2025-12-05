from threading import *
import time

print("Main Thread Name :",current_thread().name)
print("Current thread identification number :",current_thread().ident)
def show():
    # current_thread().name="Aniket"
    print("current thread name :",current_thread().name)
    print("current thread identification number :",current_thread().ident)

th1=Thread(target=show,name="Dynamo")
th2=Thread(target=show,name="Mortal")
print("Active Thread count :",active_count())
th1.start()
th2.start()
print("Active Thread count",active_count())
time.sleep(5)
print("Active Thread count",active_count())


