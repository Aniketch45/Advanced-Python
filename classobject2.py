class Myadd:
    def add(self,x,y):
        print("self:",self)
        self.a=x
        self.b=y
        print("sum=",self.a+self.b)

    def multi(self):
       print(self.a*self.b)

n1=int(input("enter first value:"))
n2=int(input("enter second value:"))
ad1=Myadd()
ad1.add(n1,n2)
ad1.multi()




# class Myadd:
#     def add(self):
#         print("self:",self)
#         self.a=10
#         self.b=20
#         print("sum=",self.a+self.b)
#
#     def sub(self):
#         #self.a=30
#         print(self.a-self.b)
#
#     def multi(self):
#         print(self.a*self.b)
#
# ad1=Myadd()
# ad1.add()
# ad1.sub()
# ad1.multi()
# print("***********************")
# ad2=Myadd()
# ad2.add()