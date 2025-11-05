# import gc

# gc.enable()
# print(gc.isenabled())

#destructor
'''import time as t
class Garbagecoll:
    def __init__(self):
        print("hello")

    def __del__(self):
        print("Performing Clean up Activity")

g1=Garbagecoll()
print("it is in use")
t.sleep(5)
print("Work done with g1")
g1=None
t.sleep(10)
print("End od Application")'''

# import time as t
# class Destructor:
#     def __init__(self):
#         print("constructor")
    
#     def __del__(self):
#         print("Destructor cleanup Activity")

# t1=Destructor()
# t2=t1
# t3=t2
# del t1
# t.sleep(2)
# print("object not Destroyed")
# del t2
# t.sleep(2)
# print("object not Destroyed")
# del t3
# t.sleep(2)
# print("end of application")

# import time as t
# class Destructor:
#     def __init__(self):
#         print("constructor")
    
#     def __del__(self):
#         print("Destructor is doing cleanup Activity")

# t1=[Destructor(),Destructor(),Destructor()]
# t.sleep(2)
# t1=None

import sys 
class Destructor:
    def __init__(self):
        print("constructor")
    
    def __del__(self):
        print("Destructor is doing cleanup Activity")

t1=Destructor()
t2=t1
t3=t2
print("total reference count is : ",sys.getrefcount(t3))  #ans 4 b'coz self is also a reference varible