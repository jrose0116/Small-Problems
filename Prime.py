def prime(x):
    if(x == 1 or x == 0):
        return False
    for i in range(x-1)[1:]:
        if(x//i == x/i and i!=1 and i!=x):
            return False
    return True

print("7: ", prime(7))
print("4: ", prime(4))
print("10: ", prime(10))
print("1: ", prime(1))
print("0: ", prime(0))
print("13: ", prime(13))
print("15: ", prime(15))
print("17: ", prime(17))