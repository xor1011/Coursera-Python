#self calling functions

def My_Factorial(n):
    if (n==1):
        return 1
    else:
        return n*My_Factorial(n-1)
print(My_Factorial(5))
