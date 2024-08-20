

"""using list related python methods()"""

def avgMean(lst):
    return sum(lst)/len(lst)

lst=[10,20,30,40]
avg=avgMean(lst)
print(avg)

""" Iterative approach """

def avgmean(lst):
    sum=0
    for i in range(len(lst)):
        sum+=lst[i]
    return sum/len(lst)

lst=[10,20,30,40]
aVG=avgmean(lst)
print(aVG)