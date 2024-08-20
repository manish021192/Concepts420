"""
SELECTION SORT
The selection sort algorithm sorts an array by repeatedly finding the minimum element
(considering ascending order) from unsorted part and putting it at the beginning. The
algorithm maintains two sub arrays in a given array.

1) The subarray which is already sorted.

2) Remaining subarray which is unsorted. In every iteration of selection sort, the minimum
element (considering ascending order) from the unsorted subarray is picked and moved to the
sorted subarray.

initial list : 64, 25, 12, 22, 11
step 1 : 11 , 64 , 25 , 12 , 22
step 2 : 11 , 12 , 64 , 25 , 22
step 3 : 11 , 12 , 22 , 25 , 64

time complexity is O(n*n)
"""


def selectSort(lst):
    n = len(lst)
    for i in range(n - 1):
        min_ind = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_ind]:
                min_ind = j
        lst[min_ind], lst[i] = lst[i], lst[min_ind]
        print(lst)

lst = [64,25,12,22,11]

selectSort(lst)
print(*lst)