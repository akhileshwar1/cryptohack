from mod_arithmetic import extended_gcd
# E:Y^2 =X^3+497X+1768 mod 9739
# Given above is an elliptic curve, it is basically a cubic equation that behaves like a good trapdoor function.
# When you start from a point p, and add p to itself multiple times, what you end up lets call it p' tends to be something
# irreversible, i.e you can't find p from p'.
# The mod at the end converts a curve into a finite field. Using an unbounded curve is dangerous because attackers
# can use calculus to sniff out patterns.
# the bounds of a field limits the search space just enough so that it can't be brute forced and it also allows efficient
# operations to be implemented on the hardware.
# so for 9379 as our mod, we will have 9379 points on our graph. For an attacker to decipher the secret key given P,
# g(generator), he will have to guess ka*kbp where which is somewhere below 9739?
# yes, but the caveat is that  while iterating over 9739 space, we will have to compute g1, g2, g3.... so on
# and each computation is quite heavy since they are elliptic curve multiplications. so even though the key space is
# small each computation is heavier and that hardens the security. kind of inverse of mod exponentiation where the
# individual ops were relatively lighter but then the key space had to be huge.
# This is an alternative to DH key exchange, the advantage here is that the key sizes are smaller resulting in higher
# performance in terms of memory consumption and faster encryption/decryption.

px = 8045
py = 6936
# find point Q such that p + q = O where O is infinity. We know the answer is -p.
# When adding a point P to its inverse −P, the line through P and −P is vertical.
# This vertical line does not intersect the curve at any other finite point, so the result is ∞.
print("the point q is %d, %d", px, -py%9739)

def is_infinity(p):
    if (p[0] == None and p[1] == None):
        return True
    return False

def mod_add(a, b, p):
    return (a + b) % p

def mod_sub(a, b, p):
    return (a - b) % p

def mod_mult(a, b, p):
    return (a * b) % p

def mod_div(a, b, p):
    inverse = extended_gcd(b, p)[0] # modular inverse of the denominator, since div is undefined in finite field.
                                    # for example: 2/4 mod 6 is 0.5 mod 6 and there is no equivalence here. Where will it be wrapped?
                                    # so we redefine division as multiplication with the modular inverse of the denominator.
    return (a * inverse) % p

# point addition
# NOTE: IN mod arithmetic, operations like add, sub, mult take a, b inside the field and output something inside the field.
def point_addition(P, Q, a, p):
    if (is_infinity(P) and is_infinity(Q)):
        return (-1, -1)
    elif(is_infinity(P)):
        return Q
    elif(is_infinity(Q)):
        return P
    elif(P[0] == Q[0] and P[1] == -Q[1]): # vertical line that passes through infinity.
        return (-1, -1)
    else:
        x1, y1, x2, y2 = P[0], P[1], Q[0], Q[1]
        slope = -1
        if (x1 == x2 and y1 == y2): # P = Q
            numerator = mod_mult(3, (pow(x1, 2, p)), p)
            numerator = mod_add(numerator, a, p)
            denominator = mod_mult(2, y1, p)
            slope = mod_div(numerator, denominator, p)
        else: # P != Q
            numerator = mod_sub(y2, y1, p)
            denominator = mod_sub(x2, x1, p)
            slope = mod_div(numerator, denominator, p)

        x3 = mod_sub(pow(slope, 2, p), x1, p)
        x3 = mod_sub(x3, x2, p)
        y3 = mod_mult(slope, mod_sub(x1, x3, p), p)
        y3 = mod_sub(y3, y1, p)
        return (x3, y3)

p = 9739
a = 497

# checks.
print(point_addition((5274, 2841), (8669, 740), a, p))
print(point_addition((5274, 2841), (5274, 2841), a, p))

P = (493, 5564)
Q = (1539, 4742)
R = (4403, 5202)
PP = point_addition(P, P, 497, 9739)
QR = point_addition(Q, R, 497, 9739)
S = point_addition(PP, QR, 497, 9739)
print("point addition is", S)

# double and add algorithm for performing scalar multiplication.
# O(log n) instead of O(n)
def multiply_point(P, n, O, p, a):
    Q = P
    R = O  # Set R = O (point at infinity)

    while n > 0:
        if n % 2 == 1:  # If n is odd
            R = point_addition(R, Q, a, p)  # R = R + Q, basically returns the same point.
        Q = point_addition(Q, Q, a, p)  # Q = [2]Q
        n //= 2  # n = ⌊n/2⌋

    return R

P = (2339, 2213)
print("scalar multiplying P 7863 times is", multiply_point(P, 7863, (None, None), p, a))
