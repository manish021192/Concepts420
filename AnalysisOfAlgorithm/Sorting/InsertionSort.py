"""
Insertion sort is a simple sorting algorithm that works similar to the way you sort playing
cards in your hands. The array is virtually split into a sorted and an unsorted part. Values
from the unsorted part are picked and placed at the correct position in the sorted part.



"""

def insertionSort(l):
    for i in range(1,len(l)):
        x = l[i]
        j = i-1
        while j>=0 and x<l[j]:
            l[j+1] = l[j]
            j = j-1
        l[j+1] = x


l = [20, 5, 40, 60, 10, 30]

insertionSort(l)
print(*l)