#2 Creating thread with extending class

# from threading import *
# import time
# class Mythread(Thread):
#     def run(self):
#         for i in range(4):
#             print("Yes hello")
#             time.sleep(2)

# m2=Mythread()
# m2.start()

# for i in range(4):
#     print("main Thread")
#     time.sleep(2)

#3 extended thread without run method
# from threading import *
# import time
# class Mythread(Thread):
#     def display(self):
#         for i in range(3):
#             print(current_thread())
#             print("hello Develo")
#             time.sleep(2)

# m2=Mythread()
# th=Thread(target=m2.display)
# th.start()

# for i in range(4):
#     print("main Thread")
#     time.sleep(2)

#4 without extending
# from threading import *
# import time
# class Work():
#     def run(self):
#         print("Done")

#     def display(self):
#         for i in range(4):
#             print(current_thread())
#             print("hello")
#             time.sleep(2)
    
# w1=Work()
# th=Thread(target=w1.display)
# th.start()
# w1.run()




# 1
# from threading import *
# import time
# print("Welcome")

# def display():
#         for i in range(3):
#             print("welcome to pcmc")
#             print("current thread",current_thread().getName())
#             time.sleep(1)

# def show():
#        for i in range(3):
#             print("welcome to mumbai")
#             print("current thread",current_thread())
#             time.sleep(1)

# thread1=Thread(target=show)
# thread2=Thread(target=display)

# thread1.start()
# thread2.start()
# print("Thank You")


#withount threading time
# import time
# class Demo():
#     def square(self,x):
#         for i in x:
#             print("Square is :",i*2)
    
#     def double2(self,x):
#         for i in x:
#             print("double is :",i*i)

# num=[1,2,3,4,5]
# th1=Demo()
# begintime=time.time()
# th1.square(num)
# th1.double2(num)
# endtime=time.time()
# print("Total time is :",endtime-begintime)

#with threading time
# from threading import *
# import time

# class Demo(Thread):
#     def square(self,x):
#          for i in x:
#            print("Square is :",i*2)
#            time.sleep(1)
    
#     def double2(self,x):
#        for i in x:
#              print("double is :",i*i)
#              time.sleep(1)
    

# num=[1,2,3,4,5]
# d=Demo()
# th1=Thread(target=d.square,args=(num,))
# th2=Thread(target=d.double2,args=(num,))
# begintime=time.time()
# th1.start()
# th2.start()
# th1.join()
# th2.join()
# endtime=time.time()
# print("Total time :",endtime-begintime)


