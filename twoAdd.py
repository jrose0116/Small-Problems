# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

def twoadd(arr,k):
    if(len(arr)<=1):
        return False
    i = 0
    while(i<len(arr)):
        j=i+1
        while(j<len(arr)):
            if(arr[i]+arr[j]==k):
                print(arr[i]," + ",arr[j]," = ",k)
                return True
            j+=1
        i+=1
    return False
    
print(twoadd([10,15,3,7],17))
print(twoadd([10,15,20,25],20))
print(twoadd([5,10,15,20,25],20))