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

from threading import *
import time
print("Entered in Threads")
class Demo():
    def func(self):
        for i in range(4):
            print("Hello Welcome")
            time.sleep(2)
            print("Thread Name :",current_thread().name)

    def func2(self):
        for i in range(4):
            print("done")
            time.sleep(2)
            print("Thread Name :",current_thread().name)

print("Exiting from main")
print(current_thread().name)
    
m2=Demo()
th=Thread(target=m2.func)
th2=Thread(target=m2.func2)
th.start()
th2.start()



