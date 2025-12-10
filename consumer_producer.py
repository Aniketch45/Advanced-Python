# from queue import *

# q=PriorityQueue()
# q.put((1,'Aniket'))
# q.put((2,'Chirag'))
# q.put((8,'Shantanu'))
# q.put((3,'Viki'))

# while not q.empty():
#     print(q.get())

from queue import *

q=LifoQueue()
q.put('Aniket')
q.put('Chirag')
q.put('Shantanu')
q.put('Viki')

while not q.empty():
    print(q.get())


#using queue
# from threading import *
# from queue import *
# from random import *
# import time

# q=Queue()

# def producer():
#     while True:
#         print("Producer producing items..")
#         item=randint(1,100)
#         q.put(item)
#         print("item inserted")
#         time.sleep(3)

# def consumer():
#     while True:
#         print("Consumer waiting for item")
#         print("item received",q.get())
#         time.sleep(3)

# th1=Thread(target=producer)
# th2=Thread(target=consumer)
# th1.start()
# th2.start()




#using condition object
# from threading import *
# import time

# c=Condition()
# def user():
#     c.acquire()
#     print("user Booking Tickets")
#     c.wait()
#     time.sleep(2)
#     print("Ticket Recieved")
#     c.release()

# def admin():
#     c.acquire()
#     time.sleep(3)
#     print("Admin viewing information of user")
#     time.sleep(2)
#     print("Ticket confirmed by admin")
#     c.notify()        #for multiple Threads notifyall()
#     c.release()

# th1=Thread(target=user)
# th2=Thread(target=admin)
# th1.start()
# th2.start()

#using event object
# from threading import *
# import time

# e=Event()

# def consumer():
#     print("Consumer waiting for producer")
#     e.wait()
#     time.sleep(2)
#     print("Recieved Product")

# def producer():
#     time.sleep(3)
#     print("Producer Manufacturing product")
#     time.sleep(3)
#     print("Delivering Product to consumer")
#     e.set()

# th1=Thread(target=consumer)
# th2=Thread(target=producer)
# th1.start()
# th2.start()