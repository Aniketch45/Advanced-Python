# class Test:
#     def __init__(self):
#         print("this is constructor")

# t1=Test()
# t1.__init__()   #we can call constructor explicitly



# class Test:
#     def __init__(self):
#         print("this is constructor")
#         self.a=20
#         self.b=30

#     def __init__(self,x,y):   # Constructor Overloading and Overiding is not allowed in  python
#         self.a=x
#         self.b=y

   
#     def add(self):
#         print("sum=",self.a+self.b)

#     def sub(self):
#         print("sub=",self.a-self.b)

# #t1=Test()
# t1=Test(10,20)
# t1.sub()
# t1.add()



# t2=Test()
# t3=Test()

class Test:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
    def __init__(self,name,age,address,status):
        self.name=name
        self.age=age
        self.address=address
        self.status=status
    def show(self):
        print(f"my name is :{self.name}, im {self.age} Years of age and im {self.address} Lives")

t1=Test("Aniket",21,"Pune")
t1.show()