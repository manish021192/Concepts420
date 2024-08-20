


"""
DEEFINITION OF LIST:
    - dynamic sized array
    -with different type of items also within the list

ADVANTAGES OF LIST :
    -Random Access 
    -Cache Friendly

DISADVANTAGES OF LIST :
    Below operation are slow and takes linear time as each of the element are in
     contiguous memory allocation so position of each items need to be modified.
     :
        -Insertion (append and pop takes constant time but at any other place it will take
         linear time at worst case)
        -Deletion append and pop takes constant time but at any other place it will take
         linear time at worst case)
        -Search : works best in sorted Linked list otherwise it takes again linear time
        to search element in unsorted lists.

"""

List=[10,20,30,40,50,60,70,80,90,100]
print("List : " ,List)
print("pop()  in List :",List.pop())
print("List : ",List)
print("append() in List :",List.append(1000))
print("insert() in list",List.insert(3,100))

