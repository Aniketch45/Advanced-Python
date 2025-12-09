#lock Synchronization
# from threading import *
# import time

# l=Lock()
# def display():
#     l.acquire()
#     for i in range(5):
#         print("current Thread name :",current_thread().name)
#         time.sleep(1)   
#     l.release()
        
# th1=Thread(target=display,name="even")
# th2=Thread(target=display,name="odd")

# th1.start()
# th2.start()

#RLock Synchronization 
# from threading import *
# l=RLock()
# def factorial(n):
#     l.acquire()
#     if n==0:
#         result=1
#     else:
#         result=n*factorial(n-1)
#     l.release()
#     return result

# def show(n):
#     print("factorial is :",factorial(n))

# th1=Thread(target=show,args=(5,))
# th2=Thread(target=show,args=(3,))

# th1.start()
# th2.start()

#semaphor we can give counter multiple threads that allowed for resource sharing





from threading import *
l=Lock()
li3=[0]*41
for i in range(41):
    li3[i]=i
li=set(li3)

def booking(n):
    l.acquire()
    li=n
    print("Available Seats are :")
    for i in li:
        print(i)
    l.release()

seat=int(input("Enter Seat number to book :"))
th1=Thread(target=booking,args=(seat,))
th2=Thread(target=booking,args=(seat,))

th1.start()
th2.start







        