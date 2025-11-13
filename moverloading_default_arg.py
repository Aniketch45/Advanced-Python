x=(10,40,50)
y=(10,40,50)
print(id(x))
print(id(y))
print(x is y)   #immutable give true

a=[10,50,60]
b=[10,50,60]
print(id(a))
print(id(b))
print(a is b)   #mutable give false


#overloading with variable length arg
# class Add:
#     def addition(self,*a):
#         total=0
#         for i in a:
#             total+=i

#         print("Addition is",total)

# c=Add()
# c.addition()
# c.addition(10,30,49)
        
# overloading with default argument
# class Add:
#     def show(self,x=None,y=None,z=None):
#         if(x!=None and y!=None and z!=None):
#             print("Addition is :",x+y+z)
#         elif(x!=None and y!=None):
#             print("Addition is :",x+y)
#         else:
#             print("Please enter 2 arg ")

# a=Add()
# a.show(10,40)


