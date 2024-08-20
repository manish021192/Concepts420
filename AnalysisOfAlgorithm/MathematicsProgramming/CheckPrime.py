
"""APPROACH 1 - NAIVE APPROACH
Time Complexity: O(n)"""
import math


def CheckPrime(n):
    c=0
    if n<1:
       return False
    elif n==2:
       return True
    else:
       for i in range(2, n):
           if n % i == 0:
               c+=1
           else:
               continue
       if c > 0:
           return False
       else:
           return True



n=int(input("Enter the number : "))
num=CheckPrime(n)
if num==True:
    print("Prime number")
else:
    print("Not prime number")

#========================================================================================

"""APPROACH 2 using square root
Time Complexity=O(srt(n))"""

def CheckPrime(n):
    c=0
    if n<=1:
        return False
    elif n==2 or n==3:
        return True
    else:
        for i in range(2,int(math.sqrt(n))):
            if n%i==0:
                c+=1
                return False
                break
        if c==1:
            return False
        else:
            return True



n=int(input("Enter the number : "))
num=CheckPrime(n)
if num==True:
    print("Prime number")
else:
    print("Not Prime number")

#==============================================================================================

