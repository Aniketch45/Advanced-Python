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
class Demo():
    def func(self):
        print("Hello Welcome")
        time.sleep(2)

    def func2(self):
        print("Exiting")
        time.sleep(2)
    
m2=Mythread()
# th=Thread(target=m2.display)
# th.start()
# m2.start()


