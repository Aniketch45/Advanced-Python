# factorial of a number

def fact(n):
    a=0
    b=1
    f=1
    if n==1:
        return
    else:
        
        for i in range(n):
            a=b
            b=a
            f=b*fact(n-1)
             


a=fact(5)
print(a)