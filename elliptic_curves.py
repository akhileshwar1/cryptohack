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
