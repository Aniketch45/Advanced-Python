#multiple inheritance

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    # def show(self):
    #     print("person name is : ",self.name)
    #     print("Age is : ",self.age)

class Car:
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color

    def show(self):
        print("car Brand is : ",self.brand)
        print("Color is : ",self.color)

class Employee(Person, Car):  #DLR Depth left to right
    def __init__(self,name,age,brand,color):
        Person.__init__(self,name,age)
        Car.__init__(self,brand,color)
    
    # def show(self):
    #     print("child method")

e1=Employee("Aniket",21,"Mahindra","White")
e1.show()


        



#hierarchical inheritance

# class Root:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y

#     def rmethod(self):
#         print(f"x : {self.x}, y : {self.y}")

# class Branch1(Root):
#     def branch1m(self):
#         print("Add :",self.x+self.y)

# class Branch2(Root):
#     def branch2m(self):
#         print("mul : ",self.x*self.y)

# r=Branch1(30,40)
# r.rmethod()
# r.branch1m()

# r2=Branch2(30,40)
# r2.rmethod()
# r2.branch2m()



#multi level inheritance
# class grandparent():
#     def __init__(self):
#         print("grand parent Const")
    
#     def gshow(self):
#         print("Grand parent method")
    
# class parent(grandparent):
#     def __init__(self):
#         super().__init__()
#         print("parent Const")
    
#     def pshow(self):
#         print("parent method")

# class child(parent):
#     def __init__(self):
#         super().__init__()
#         print("child Const")
    
#     def cshow(self):
#         print("child method")

# c=child()
# c.gshow()
# c.pshow()
# c.cshow()



#single level inheritance
# class parent():
#     def __init__(self):
#         print("parent Const")
    
#     def pshow(self):
#         print("parent method")

# class child(parent):
#     def __init__(self):
#         super().__init__()
#         print("child Const")
    
#     def cshow(self):
#         print("child method")

# c=child()
# c.pshow()
# c.cshow()

