from mod_arithmetic import extended_gcd
import hashlib
from Crypto.Util.number import *

print(pow(101, 17, 22663))
print(pow(12, 65537, 17*23))
print(857504083339712752489993810776 * 1029224947942998075080348647218)

# d ≡ e−1modϕ(N) where d is the decryption key and e is the encryption key.
# or in other words ed = 1 modϕ(N)
# this can be calculated by getting the coefficients using egcd where ex + Ny = gcd(e, N) and x is the answer.
# Note that this is because we know e and n are coprime => (gcd(e, N) = 1) => (ex + Ny = 1)
# and that x can be found using the egcd algorithm.
d = extended_gcd(65537, 857504083339712752489993810776 * 1029224947942998075080348647218)[0]
print(d)

N = 882564595536224140639625987659416029426239230804614613279163
e = 65537
c = 77578995801157823671636298847186723593814843845525223303932 

# (m^e = c) => (c^d = m mod N), where m is the message.
# how beautiful is modulo arithmetic! Look at the way that c^d is wrapped back to m in the field!
# basically you take the message m, and raise it to eth power in the field of some prime N.
# for an attacker to get the message back, assuming he has N and e, he will have to factorise N into
# p and q to get d, since (ed = 1 mod ϕ(N)) and ϕ(N) is = (p-1)(q-1)
# the central idea is that: there are two powers in the field N that are muliplicative inverses of each other,
# one gives you the ciphertext, and the other when applied to the ciphertext gives you the plaintext back.
plaintext = pow(c, d, N)
print(plaintext)


m = "crypto{Immut4ble_m3ssag1ng}"
hash_object = hashlib.sha256()
hash_object.update(m.encode('utf-8'))
hex_dig = hash_object.hexdigest()
m_hash = bytes_to_long(bytes.fromhex(hex_dig))

print(m_hash)

N = 15216583654836731327639981224133918855895948374072384050848479908982286890731769486609085918857664046075375253168955058743185664390273058074450390236774324903305663479046566232967297765731625328029814055635316002591227570271271445226094919864475407884459980489638001092788574811554149774028950310695112688723853763743238753349782508121985338746755237819373178699343135091783992299561827389745132880022259873387524273298850340648779897909381979714026837172003953221052431217940632552930880000919436507245150726543040714721553361063311954285289857582079880295199632757829525723874753306371990452491305564061051059885803
d = 11175901210643014262548222473449533091378848269490518850474399681690547281665059317155831692300453197335735728459259392366823302405685389586883670043744683993709123180805154631088513521456979317628012721881537154107239389466063136007337120599915456659758559300673444689263854921332185562706707573660658164991098457874495054854491474065039621922972671588299315846306069845169959451250821044417886630346229021305410340100401530146135418806544340908355106582089082980533651095594192031411679866134256418292249592135441145384466261279428795408721990564658703903787956958168449841491667690491585550160457893350536334242689

# why do you see sign the hash of the message and not the message itself?
# The receiver has the original message (M) decrypted using his private key, and also has the hash (H) decrypted using the 
# sender's public key, now if h(M) == H then we can be sure that the message wasn't tampered with.
# Always use seperate keys for encryption and signature.
signed_message = pow(m_hash, d, N)
print("signed message is")
print(signed_message)

# NOTE: This means that if gcd(m, n) = 1, then φ(m) φ(n) = φ(mn). Proof outline: Let A, B, C be the sets of positive integers which are coprime to and less than m, n, mn, respectively, so that |A| = φ(m), etc. Then there is a bijection between A × B and C by the Chinese remainder theorem. 

# NOTE: We don't count φ(n) by iterating till n and find if each integer is coprime because that will involve taking the gcd for each of the numbers.
# In effect, it will take n * O(i=1∑n−1log(i)), and n is huge. Therefore prime factorization is better, but even that requires advanced methods and they too fall short for very large n.
# like something in the range of 2048 bits i.e 256 bytes! for comparison, an int type is just 4 bytes. 2^32 = 4294967296.

# NOTE: our gcd roughly makes the next number in contention to half so we can say, O(log2min(a, b)), but this implicitly assumes that division is O(1).
# For larger numbers division is not O(1) and it will dominate the time complexity!

# NOTE: 829 bits N was factorized in 2020 or so. Good for a decade or so now. Quantum can break rsa in the future.
