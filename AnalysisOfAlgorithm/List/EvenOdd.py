

def evenOdd(lst):
    lstE=[]
    lstO=[2]
    for i in range(len(lst)):
        if lst[i]%2==0:
            lstE.append(lst[i])
        else:
            lstO.append(lst[i])
    return lstE,lstO

lst=[10,13,57,68,90,46]
even,odd=evenOdd(lst)
print("Even lis : " ,even )
print("Odd lis : " ,odd )

#Using List comprehension

def evenODD(lst):
    lstone=[]
    lsttwo=[]
    lstone=[i for i in range(len(lst)) if i%2==0]
    print("Even list one :" ,lstone)
    lsttwo = [i for i in range(len(lst)) if i % 2 != 0]
    print("Odd list two :",lsttwo)

lst=[10,13,57,68,90,46]
evenODD(lst)