def bubblesort(arr):
    prev=[]
    for i in range(len(arr)): #Will not take more iterations than the amount of elements to sort
        j=0
        while (j<len(arr)-1):
            if(arr[j]>arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
            j+=1
    return arr

a = bubblesort([7,3,5,4,2])
b = bubblesort([])
c = bubblesort([7])
d = bubblesort([5,4,3,2])
e = bubblesort([7,7,5,8])
f = bubblesort([4,4,4,4,4,4,4,4])
g = bubblesort([5,7,4,4])

print("Final Results:")
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)