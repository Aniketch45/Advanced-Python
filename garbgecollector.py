# import gc

# gc.enable()
# print(gc.isenabled())

#destructor
import time as t
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
print("End od Application")
