
def getSmallerElements(lst,ele):
    lstoutput=[]
    for i in range(len(lst)):
        if ele > lst[i]:
            lstoutput.append(lst[i])
    return lstoutput

lst=[14,34,5,6,7,8,9,34,25,367,865,444,55,22,11,33,77,88,99]
inp=int(input("Enter the number for which you to find lesse list "))
output=getSmallerElements(lst,inp)
print(output)

