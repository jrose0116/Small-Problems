def selectionsort(arr):
    for i in range(len(arr)):
        curr = i
        for j in range(len(arr))[i:]:
            if(arr[j] < arr[curr]):
                curr = j
        temp = arr[i]
        arr[i] = arr[curr]
        arr[curr] = temp
    return arr

a = selectionsort([7,3,5,4,2])
print("\n")
b = selectionsort([])
print("\n")
c = selectionsort([7])
print("\n")
d = selectionsort([5,4,3,2])
print("\n")
e = selectionsort([7,7,5,8])
print("\n")
f = selectionsort([4,4,4,4,4,4,4,4])
print("\n")
g = selectionsort([5,7,4,4])
print("\n")

print("\n\nFinal Results:")
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)