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
# The idea here is that we can see the gcd(x,y) = ax + by.
# This actually is nothing but an effect of seeing both x and y in terms of the gcd.
# How? What does division even mean? Firstly, I see every number in terms of single units i.e 1.
# and then addition simply means joining multiple 1's together.
# subtraction is the opposite.
# multiplication is addition performed n times.
# division is looking at the result of multiplication and seperating/grouping 1's at n boundaries.
# kind of like this II II II is 6. and as you can see it is 2 added 3 times. and division is value in each bucket: II.
# power is nothing but multiplication applied n times.
def extended_gcd(x, y):
    numerators = []
    denominators = []
    quotients = []
    remainders = []
    num = max(x,y)
    denom = min(x,y)

    while (denom != 0):
        quotient = num//denom
        rem = num % denom
        numerators.append(num)
        denominators.append(denom)
        quotients.append(-quotient)
        remainders.append(rem)
        num = max(rem, denom)
        denom = min(rem, denom)

    print(numerators)
    print(denominators)
    print(quotients)
    print(remainders)

    map_results = {}
    prev_quot = 1
    for rem, quot, denom, num in zip(remainders[::-1], quotients[::-1], denominators[::-1], numerators[::-1]):
        if (rem == 0):
            continue

        if (num not in map_results):
            map_results[num] = prev_quot
        else:
            map_results[num] = map_results[num] + prev_quot

        if (denom not in map_results):
            map_results[denom] = quot * prev_quot
        else:
            map_results[denom] = map_results[denom] + (quot * prev_quot)

        prev_quot = map_results[denom]


    return map_results[x], map_results[y]



print(extended_gcd(12,8))
print(extended_gcd(64,36))
print(extended_gcd(26513,32321))

# ---------------------------------------------------------------------------------------------------------

