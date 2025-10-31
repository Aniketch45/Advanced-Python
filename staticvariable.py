#Ddeclaring static variable
class Test:
    a=10  #directly inside the class
    def __init__(self):
        Test.b=20     #inside constructor using class name

    def m1(self):
        Test.c=30    #inside instance method using class name

    @classmethod
    def m2(cls):
        Test.d=40      #inside class method using class name or cls
        cls.e=50

    @staticmethod
    def m3():          #inside static method using class name
        Test.f=60

print("a=",Test.a)
t1=Test()
print("b=",Test.b)
t1.m1()
print("c=",Test.c)
#Test.m2()
t1.m2()
print("d=",Test.d)
print("e=",Test.e)
t1.m3()
print("f=",Test.f)



# class Test:
#     a=10     #static variable
#     def __init__(self):
#         self.b=20  #instance variable
#
# print("a=",Test.a)
# #print("b=",Test.b) #error
# t1=Test()
# t2=Test()
# print("t1.a=",t1.a)
# print("t1.b=",t1.b)
# print("Instance variable of t1:",t1.__dict__)
# print("Instance variable of t2:",t2.__dict__)
# print("**********************")
# print("t2.a=",t2.a)
# print("t2.b=",t2.b)
# print("**********************")
# Test.a=100
# print("t1.a=",t1.a)
# print("t2.a=",t2.a)
# print("****************************")
# t1.b=200
# print("t1.a=",t1.a)#100
# print("t1.b=",t1.b)#200
# print("t2.a=",t2.a)#100
# print("t2.b=",t2.b)#20
# print("**************************")
# t1.a=1000
# print("Instance variable of t1:",t1.__dict__)
# print("Instance variable of t2:",t2.__dict__)
# print("t1.a=",t1.a)
# print("t2.a=",t2.a)