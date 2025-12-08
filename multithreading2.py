# from threading import *
# import time
# class Mythread(Thread):
#     def run(self):
#         print(current_thread())

#     def display(self):
#         for i in range(3):
#             print(current_thread())
#             print("hello Develo")
#             time.sleep(2)

# m2=Mythread()
# th=Thread(target=m2.display)
# th.start()
# m2.start()

# for i in range(4):
#     print("main Thread")
#     time.sleep(2)

# from threading import *
# import time
# print("Entered in Threads")
# class Demo():
#     def func(self):
#         for i in range(4):
#             print("Hello Welcome")
#             time.sleep(2)
#             print("Thread Name :",current_thread().name)

#     def func2(self):
#         for i in range(4):
#             print("done")
#             time.sleep(2)
#             print("Thread Name :",current_thread().name)

# print("Exiting from main")
# print(current_thread().name)
    
# m2=Demo()
# th=Thread(target=m2.func)
# th2=Thread(target=m2.func2)
# th.start()
# th2.start()

#is_alive()
from threading import *
import time

def demo():
    for i in range(2):
        print("thread name",current_thread().name)
        time.sleep(2)

t1=Thread(target=demo,name="Aniket")
t2=Thread(target=demo,name="Viki")
t3=Thread(target=demo,name="Omkar")

t1.start()
t2.start()
t3.start()
print("t1 is Thread alive :",t1.is_alive())
print("t2 is Thread alive :",t2.is_alive())
print("t3 is Thread alive :",t3.is_alive())
t1.join(5)
print("t1 is Thread alive :",t1.is_alive())
print("t2 is Thread alive :",t2.is_alive())
print("t3 is Thread alive :",t3.is_alive())
time.sleep(5)
print("t1 is Thread alive :",t1.is_alive())
print("t2 is Thread alive :",t2.is_alive())
print("t3 is Thread alive :",t3.is_alive())


