def sumOfDigits(n):
    if n<=1:
        return n

    return sumOfDigits(n//10)+n%10


n=int(input("Enter the number to print nth factorial "))
print(sumOfDigits(n))