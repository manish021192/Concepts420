# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

"""Approach 1
Time Complexity: O(n)"""
def findSum(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    return sum

n=int(input("Enter the number : "))
sum=findSum(n)
print("Sum of first" ,n,"natural numbers is : " ,+ sum)


# ==========================================================================================


"""Approach 2
Time Complexity: O(1)"""
def findSum(n):
    return int(n*(n+1)/2)

n=int(input("Enter the number : "))
sum=findSum(n)
print("Sum of first" ,n,"natural numbers is : " ,+ sum)


# ========;================================================================================
"""Approach 3
Time Complexity :O(1)
this will avoid overflow error
"""
def findSum(n):
    if n%2==0:
        return (n/2)*(n+1)
    else:
        return n*((n+1)/2)
n=int(input("Enter the number : "))
sum=findSum(n)
print("Sum of first" ,n,"natural numbers is : " ,+ int(sum))
