
"""
Time complexity : O(n)
"""

def maxElement(lst):
    if not lst:
        return None
    else:
        max = lst[0]
        for i in range(1,len(lst)):
            if lst[i]>max:
                max=lst[i]
        return max
def secondMaxElement(lst,max):
    if not lst:
        return None
    else:
        max1=lst[0]
        for i in range(1,len(lst)):
            if lst[i]<max and lst[i] > max1:
                max1=lst[i]
        return max1


lst=[12,45,21,88,65,78,43,56,1345]
element=maxElement(lst)
print("max element is : ",element)
secondmax=secondMaxElement(lst,element)
print("max element is : ",secondmax)


"""Efficient SOlution
Time complexity=THETA(n)
"""

def another_Sec_max(lst):
    if not lst:
        return None
    else:
        max=lst[0];slar=None
        for i in range(1,len(lst)):
            if lst[i]>max:
                slar=max
                max=lst[i]
            elif lst[i]!=max:
                if slar==None or slar<lst[i]:
                    slr=lst[i]
        return slar

lst=[12,45,21,88,65,78,43,56,1345]
element=another_Sec_max(lst)