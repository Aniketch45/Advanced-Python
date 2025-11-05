# has A relationship in composition
# class Mat:
#     x=30
#     def __init__(self):
#         self.y=12

#     def m1(self):
#         print("Addition is : ",self.x+self.y)

# class Calc:
#     def __init__(self):
#         self.m=Mat()
    
#     def m2(self):
#         print("x=",self.m.x)
#         print("y=",self.m.y)
#         self.m.m1()

# c1=Calc()
# c1.m2()

#passing args using another class object in composition
# class Mat:
#     x=30
#     def __init__(self,y):
#         self.y=y

#     def m1(self):
#         print("Addition is : ",self.x+self.y)

# class Calc:
#     def __init__(self,a,b):
#         self.m=Mat(a)
#         self.b=b
    
#     def m2(self):
#         print("x=",self.m.x)
#         print("y=",self.m.y)
#         print("b=",self.b)
#         self.m.m1()

# c1=Calc(10,33)
# c1.m2()

class Person:
    def __init__(self,name,age,mobile,dep,post,salary,brand,modname,ftype,price,color):
        self.name=name
        self.age=age
        self.mobile=mobile
        self.e1=Employee(dep,post,salary,brand,modname,ftype,price,color)
    
    def detail(self):
        print(f"Person Name is:{self.name}")
        print(f"Person age is:{self.age}")
        print(f"Person Mobile number is:{self.mobile}")
        self.e1.show()
        

class Car:
    def __init__(self,brand,modname,ftype,price,color):
        self.brand=brand
        self.modname=modname
        self.ftype=ftype
        self.price=price
        self.color=color
    
    def carmethod(self):
        print(f"Car Brand is :{self.brand}")
        print(f"Car Model is : {self.modname}")
        print(f"Car Fuel Type is :{self.ftype}")
        print(f"Car Price is :{self.price}")
        print(f"Car Color is :{self.color}")

class Employee:
    def __init__(self,dep,post,salary,brand,modname,ftype,price,color):
        self.dep=dep
        self.post=post
        self.salary=salary
        self.c1=Car(brand,modname,ftype,price,color)
    
    def show(self):
        print(f"Employee Depatment is :{self.dep},Employee Position is :{self.post},Employee Salary is:{self.salary}")
        self.c1.carmethod()


ename=input("Enter Person Name :")
age=int(input("Enter age of Person :"))
mob=input("Enter Mobile Number :")
dep=input("Enter Emloyee Department :")
pos=input("Enter Emloyee Position:")
sal=int(input("Enter Emloyee Salary:"))
brand=input("Enter Car Brand :")
modelname=input("Enter Model Name :")
ftype=input("Enter Fuel Type :")
price=int(input("Enter Price :"))
color=input("Enter Color :")

p1=Person(ename,age,mob,dep,pos,sal,brand,modelname,ftype,price,color)
p1.detail()
        