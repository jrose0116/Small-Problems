def nonAdjacentSum(arr):
    if(len(arr) == 1):
        return arr[0]
    if(len(arr) == 0):
        return 0
    use = arr[0] + nonAdjacentSum(arr[2:])
    lose = nonAdjacentSum(arr[1:])
    if(arr[0] >= max(use, lose)): #For Negative Case
        return arr[0]
    return max(use,lose)

print(nonAdjacentSum([1,2,3,4,5])) #9
print(nonAdjacentSum([-2,-1,-3,-4,-5])) #-1
print(nonAdjacentSum([2,4,6,2,5])) #13
print(nonAdjacentSum([5,1,1,5])) #10
print(nonAdjacentSum([0,0,0,0])) #0

