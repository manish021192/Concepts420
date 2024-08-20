
# Time complexity : O(n)


def linearSearch(lst,n):
    for i in range(len(lst)):
        if lst[i]==n:
            print("Element found at : " , i+1 ,"position")
            return
        else:
            continue
    print("element not find")




lst=[23,45,67,83,11,23]
n=83
linearSearch(lst,n)