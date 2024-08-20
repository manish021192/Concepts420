
"""
Time complexity : O(N)
"""

def maxElement(lst):
    if not lst:
        return None
    else:
        max = lst[0]
        for i in range(len(lst)):
            if lst[i]>max:
                max=lst[i]
        return max


lst=[12,45,21,88,65,78,43,56,1345]
element=maxElement(lst)
print("max element is : ",element)

"""Efficient SOlution
Time complexity=THETA(n)
"""