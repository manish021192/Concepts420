
"""
Approach 1

"""

def CountDigit(n):
    c=0;
    while(n>0):
        n=int(n/10)
        c=c+1
    return c

n=int(input("Enter the number : "))
count=CountDigit(n)
print("Total digits : " ,count)