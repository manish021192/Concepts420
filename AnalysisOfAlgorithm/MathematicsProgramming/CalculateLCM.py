
"""Approach 1
Time complexity is O(a*b - max(a,b))"""

def CalculateLCM(a,b):
    res=max(a,b)
    while True:
        if res%a==0 and res%b==0:
            return res
        res+=1




a=int(input("Enter the number a :"))
b=int(input("Enter the number 2 :"))
lcm=CalculateLCM(a,b)
print("LCM of ",a,"&",b,"is : " ,lcm)

