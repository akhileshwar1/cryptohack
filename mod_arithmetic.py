def gcd(x , y):
    if (x == y):
        return x
    elif(x > y):
        return gcd(x-y, y) # instead of -, what if we use %, you see the next greatest in contention will be the remainder.
                           # but in that case stop at the case where the remainder is 0.
    else:
        return gcd(x, y-x)

def eff_gcd(x, y):
    if (x == 0):
        return y
    elif (y == 0):
        return x
    elif (x == y):
        return x
    elif (x > y):
        return gcd(x%y, y)
    else:
        return gcd(x, y%x)

print(gcd(66528, 52920))
print(eff_gcd(66528, 52920))

# ---------------------------------------------------------------------------------------------------------
