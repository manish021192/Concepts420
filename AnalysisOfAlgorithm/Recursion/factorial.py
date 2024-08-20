
def calcuateFactorial(n):
    if n<0:
        return 0
    elif n<=1:
        return 1
    else:
        return n * calcuateFactorial(n-1)


n=int(input("Enter the number to print nth factorial "))
print(calcuateFactorial(n))