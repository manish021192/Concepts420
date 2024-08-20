
# TimeCompleity =O(logn)
def binarySearch(mylist,front,rear,ele):
#     CHeck base case
    if rear>=front:
        mid=front+(rear-front)//2
        if mylist[mid]==ele:
            print("element found at ",mid)
        elif mylist[mid]>ele:
            return binarySearch(mylist,front,mid-1,ele)
        elif mylist[mid]<ele:
            return binarySearch(mylist,mid+1,rear,ele)
    else:
        print("element not present")


mylist=[10,20,30,40,50,60,70,80,90,100,110,120]
size=len(mylist)
ele=70
binarySearch(mylist,0,size-1,ele)