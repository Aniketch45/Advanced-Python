# class employee:
#     dept_name="IT"
#     ocount=0
#     def __init__(self,eid,ename):
#         self.eid=eid
#         self.ename=ename
#         employee.ocount+=1
    
#     def show(self):
#         print("Self : ",self)
#         print("Employee name :",self.ename,"Id : ",self.eid)
    
#     @classmethod
#     def objectcount(cls):
#         print("object created",employee.ocount,"Times")

#     @classmethod
#     def clsmethod(cls):
#         print("cls : ",cls)
#         print("Employee Department is : ",cls.dept_name)

# employee.clsmethod()
# e1=employee(101,"Aniket")
# # e1.show()

# e2=employee(104,"Chirag")
# # e2.show()

# e4=employee(104,"Viki")
# e7=employee(100,"Shantanu")
# e9=employee(203,"hello")
# e3=employee(104,"Chirag")
# employee.objectcount()


class Animal:
    aname="Lion"

    def __init__(self,name):
        self.name=name

    @classmethod
    def clsmethod(cls):
        print("cls :",cls)
        print("Animal is :",cls.aname)

    def show(self):
        print("self : ",self)
        print("Animal is : ",self.name)

Animal.clsmethod()
a1=Animal("Jiraf")
a1.show()