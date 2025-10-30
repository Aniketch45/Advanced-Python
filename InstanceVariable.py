#2.delete instance variable

class Test:
    def __init__(self):
        self.a=10      #inside constructor
        self.b=20
    def show(self):
        print("a=",self.a)
        print("b=",self.b)

    def add(self):
        self.c=30    #inside instance method
        print("sum=",self.a+self.c)  #access using self
        del self.a

t1=Test()
print("t1 instance variable:",t1.__dict__)
t1.add()
print("t1 instance variable:",t1.__dict__)
#t1.show()
print("*************************************")
t2=Test()
t2.show()
print("t2 instance variable:",t2.__dict__)
t2.add()
print("t2 instance variable:",t2.__dict__)
del t1.b
print("t1 instance variable:",t1.__dict__)
print("t2 instance variable:",t2.__dict__)

#1.creating instance variable

# class Test:
#     def __init__(self):
#         self.a=10      #inside constructor
#
#     def add(self):
#         self.b=20     #inside instance method
#         print("sum=",self.a+self.b)  #access using self
#
#     def show(self):
#         print("c=:",self.c)
#
# t1=Test()
# t1.add()
# print("t1 instance variable:",t1.__dict__)
#
# t1.c=100
# print("t1.c:",t1.c)
# t1.show()
# print("t1 instance variable:",t1.__dict__)
#
# print("*********************************")
# t2=Test()
# t2.add()
# print("t2 instance variable:",t2.__dict__)