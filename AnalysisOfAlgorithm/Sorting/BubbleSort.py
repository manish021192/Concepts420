"""
Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent
elements if they are in the wrong order. This algorithm is not suitable for large data sets
as its average and worst-case time complexity is quite high.

"""

def bubbleSort(lst):
    n = len(lst)
    for i in range(n - 1):
        swapped=False
        for j in range(n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapped=True
        if swapped==False:
            return
        print(lst)

lst = [5,1,4,2,8]

bubbleSort(lst)
print(*lst)