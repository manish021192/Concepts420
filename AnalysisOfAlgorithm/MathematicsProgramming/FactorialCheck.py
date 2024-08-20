"""Apporach 1 Itertative
Time complexity = O(n)"""

def CalculateFibonacci(n):
    fv=1
    for i in range(1,n+1):
        fv*=i;
    return fv



n=int(input("Enter the number : "))
num=CalculateFibonacci(n)
print("Fibnocaii value : ",num)

#=========================================================================================

"""Approach 2
Recursion
Time Complexity = o(n)
only space complexity will be more as stack will hold each method called"""


def CalculateFibonacci(n):
    if n == 0:
        return (1)
    return (n * CalculateFibonacci(n - 1))


n=int(input("Enter the number : "))
num=CalculateFibonacci(n)
print("Fibnocaii value : ",num)