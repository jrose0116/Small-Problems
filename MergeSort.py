from heapq import merge


def mergesort(arr, tab=0): #Tab is just to make the print prettier by indented
    newarr = []
    if(len(arr) <= 1): #If length is 1 return
        print("\t"*tab*2, "Returned: ", arr)
        return arr
    if(len(arr) == arr.count(arr[0])): #If array is all one item return
        print("\t"*tab*2, "Duplicate Case - Returned: ", arr)
        return arr
    print("\t"*tab, arr)
    length = len(arr)
    if length == 1:
        return arr
    mid = length//2
    
    left = arr[:mid]
    right = arr[mid:]

    #Will recursively go down until there is one left then it will return that one as per the special case
    print("\t"*tab, "Recursive Left:")
    left = mergesort(left, tab+1)
    print("\t"*tab, "Recursive Right:")
    right = mergesort(right, tab+1)

    print("\t"*tab, "Merged: ", left, " and ", right)
    #The left and the right will always be sorted individually before this takes place or left and right will each be 1 number.
    ileft, iright = 0, 0
    while ileft < len(left) and iright < len(right):
        if left[ileft] < right[iright]:
            newarr.append(left[ileft])
            ileft+=1
        else:
            newarr.append(right[iright])
            iright+=1
    #At this point, either left or right are empty so it just adds onto the end.
    newarr += left[ileft:]
    newarr += right[iright:]
    print("\t"*tab, "Returned: ", newarr)
    return newarr;

a = mergesort([7,3,5,4])
print("\n")
b = mergesort([])
print("\n")
c = mergesort([7])
print("\n")
d = mergesort([5,4,3,2])
print("\n")
e = mergesort([7,7,5,8])
print("\n")
f = mergesort([4,4,4,4,4,4,4,4])
print("\n")
g = mergesort([5,7,4,4])

print("\n\nFinal Results:")
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)






