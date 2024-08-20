"""
SELECTION SORT
initial list : 64, 25, 12, 22, 11
step 1 : 11 , 64 , 25 , 12 , 22
step 2 : 11 , 12 , 64 , 25 , 22
step 3 : 11 , 12 , 22 , 25 , 64

time complexity is O(n*n)
"""


def selectionSort(lst):
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i]>lst[j]:
                temp=lst[i]
                lst[i]=lst[j]
                lst[j]=temp
        print(lst)

    print(lst)




lst=[64,25,12,22,11]
selectionSort(lst)