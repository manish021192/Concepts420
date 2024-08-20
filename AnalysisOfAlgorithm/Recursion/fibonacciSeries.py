def calcuateFibonacci(n):
    if n<=1:
        return n

    return calcuateFibonacci(n-1)+calcuateFibonacci(n-2)


n=int(input("Enter the number to print nth factorial "))
print(calcuateFibonacci(n))