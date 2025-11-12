# factorial of a number

def fact(n):
    if n < 0:
        return "Factorial is not defined"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)
             

num=int(input("Enter number to print factorial :"))
a=fact(num)
print(a)