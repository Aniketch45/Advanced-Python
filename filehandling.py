#Relative Path
# f=open("C:\\course\\Python\\Sample.txt","w")    #escape sequence error appear take \\ for that

#Absolute path
# f=open("sample.txt","w")     #if file i already created it overrride delete daata of that file
# f.write("Good Morning \n")
# f.write("Best of luck for the day!")
# f.read()  #notreadable
# f.close()


#Read mode
# f=open("sample.txt","r")  #read, open file if exist o.w. filenotfounderror
# a=f.read()   #function return all data
# # f.write("hello it give error not writeable")
# print(a) 
# f.close()

#append
# f=open("sample.txt","a")    #append data to Existing file 
# f.write("Good Afternoon")    #append not readable
# f.close()

#properties and fun of file object
f=open("sample.txt","r")
a=f.read()
print(a)
print("name of file",f.name)
print("mode of file",f.mode)
print("is file closed",f.closed)
print("file is readable",f.readable())
print("file is writeable",f.writable())
f.close()
print("is file closed",f.closed)














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

# l1=[10,2,30,6,7,3,99,23]
# f1=open("Even.txt","w")
# f2=open("Odd.txt","w")
# evenlist=[]
# oddlist=[]
# for x in l1:
#     if x%2==0:
#         evenlist.append(str(x)+"\n")
#     else:
#         oddlist.append(str(x)+"\n")

# f1.writelines(evenlist)
# f2.writelines(oddlist)

# f1.close()
# f2.close()

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
