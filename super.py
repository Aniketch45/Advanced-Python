# class Car:
#     a=100
#     def __init__(self):
#         self.b=50
#         print("constructor")

#     def insmethod(self):
#         print("instace method")

#     @classmethod
#     def clsmethod(cls):
#         print("Class method")

#     @staticmethod
#     def stamethod():
#         print("Static method")

# class Child(Car):
#     a=60
#     def __init__(self):
#         self.b=90
#         # print(super().a)
#         # print(self.a)
#         # print(self.b)
#         # super().__init__()
#         # print(self.b)      #using self we access parent instance member super().__init__() call first

#         # super().insmethod()
#         # super().clsmethod()
#         # super().stamethod()
    
#     def show(self):
#         print(self.b)
#         super().__init__()
#         print(self.b)
#         super().insmethod()
#         super().clsmethod()
#         super().stamethod()


# c=Child()
# c.show()

# class Child(Car):
#     a=60
#     def __init__(self):
#         self.b=90

#     @classmethod
#     def show(cls):
#         pass
#         # super().__init__()     # we cannot access instance method and construcotr in class method using super
#         # super().insmethod()
#         super(Child,cls).insmethod(cls)
#         super(Child,cls).__init__(cls)
#         # super().clsmethod()
#         # super().stamethod()

#     @staticmethod
#     def display():
#         # super().clsmethod()    #error
#         super(Child,Child).clsmethod()
#         super(Child,Child).stamethod()

# c=Child()
# c.show()
# # c.display()



# multilevel super

class GrandParent():
    def m2(self):
        print("grand parent method")

class Parent(GrandParent):
    def m2(self):
        print("parent method")

class Parent2(Parent):
    def m2(self):
        print("parent2 method")

class Child(Parent2):
    def m2(self):
        print("Child method")
        super(Parent,self).m2()
        super(Parent2,self).m2()
        Parent.m2(self)
        GrandParent.m2(self)

c1=Child()
c1.m2()