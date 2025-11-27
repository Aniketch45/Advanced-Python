# l=[2,10,5,11,14,18,3]
# f=open("Even.txt",'w+')
# f1=open("Odd.txt",'w+')
# for i in l:
#     if i%2==0:
#         f.write(str(i)+"\n")
#     else:
#         f1.write(str(i)+"\n")
       
# f.close()
# f1.close()

l1=[10,2,30,6,7,3,99,23]
f1=open("Even.txt","w")
f2=open("Odd.txt","w")
evenlist=[]
oddlist=[]
for x in l1:
    if x%2==0:
        evenlist.append(str(x)+"\n")
    else:
        oddlist.append(str(x)+"\n")

f1.writelines(evenlist)
f2.writelines(oddlist)

f1.close()
f2.close()

#isfile
# import os
# fname=input("Enter file name: ")
# x=os.path.isfile(fname)
# # from os import path as p
# # fname=input("Enter file name: ")
# # x=p.isfile(fname)

# if x:
#     f=open(fname,'r')
#     data=f.read()
#     print(data)
#     f.close()
# else:
#     print("File not found")





#w+ r+ a+ x+


# f=open("firstfile.txt",'w+')  # overrides file data and read and creates file
# f.write("Hello Aniket")
# f.seek(0)
# data=f.read()
# print(data)
# f.close()

f=open("firstfile.txt",'r+')
