def quicksort(arr, tab=0):
    print("\t"*tab,"arr: ", arr)
    if(len(arr) <= 1):
        return arr
    ipivot = len(arr)-1
    i=0
    j=ipivot-1
    while(True):
        i = 0
        j = ipivot-1
        while(arr[i]<=arr[ipivot] and i<=j):
            i+=1
        while(arr[j]>=arr[ipivot] and i<j):
            j-=1
        if(len(arr)==len(arr[:i])+len(arr[j:])):
            temp = arr[ipivot]
            arr[ipivot] = arr[i]
            arr[i] = temp
            print("\t"*tab,"left: ",arr[:i]," pivot:", arr[i]," right: ", arr[i+1:])
            return quicksort(arr[:i],tab+1)+[arr[i]]+quicksort(arr[i+1:],tab+1)
        else:
            print("\t"*tab,"else: i: ", i, " j: ",j, " pivot: ", arr[ipivot])
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            print("\t"*tab,"arr: ",arr)
    return []
    
print(quicksort([2,4,3,6,8,5,7,9,2,5,6,7,8,1,3,5]))
print(quicksort([7,3,5,4,2]))