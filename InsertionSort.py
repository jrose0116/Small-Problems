def insertionsort(arr):
    prt = ""
    for j in range(len(arr)):
        prt += str(arr[j])
    print(prt)
    for i in range(len(arr))[1:]:
        curr = arr[i]
        testIndex = i-1
        while(arr[testIndex] > curr and testIndex >= 0):
            arr[testIndex+1] = arr[testIndex]
            prt = ""
            for j in range(len(arr)):
                if(j != testIndex):
                    prt += str(arr[j])
                else:
                    prt += "*"+str(curr)+"*"
            print(prt)
            testIndex-=1
        arr[testIndex+1] = curr
    return arr

a = insertionsort([7,3,5,4,2])
print("\n")
b = insertionsort([])
print("\n")
c = insertionsort([7])
print("\n")
d = insertionsort([5,4,3,2])
print("\n")
e = insertionsort([7,7,5,8])
print("\n")
f = insertionsort([4,4,4,4,4,4,4,4])
print("\n")
g = insertionsort([5,7,4,4])
print("\n")

print("\n\nFinal Results:")
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)