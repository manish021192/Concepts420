"""Approach 1
Time complexity =theta(digit)"""

def PalindroneCheck(n):
    rev=0
    while(n>0):
        dig=n%10
        rev=(rev*10)+dig
        n=int(n/10)
    return rev


num=int(input("Enter the number : "))
n=PalindroneCheck(num)
if n==num:
    print("Palindrone number")
else:
    print("Not palindrone")