arr=[1,7,10,12,13]
arr2=[6,7,9,11,14]


def sorter(arr1,arr2):
    ptr1=0
    ptr2=0
    while ptr1<len(arr1) and ptr2<len(arr2):
        if(arr2[ptr2]<=arr1[ptr1]):
            arr.insert(ptr1,arr2[ptr2])
            ptr2+=1
        else:
            ptr1+=1
    if(ptr1>=len(arr1)):
        while ptr2<len(arr2):
            arr.append(arr2[ptr2])
            ptr2+=1
    return arr1

print(sorter(arr,arr2))