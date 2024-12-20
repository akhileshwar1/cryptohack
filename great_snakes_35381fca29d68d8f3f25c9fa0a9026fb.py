#!/usr/bin/env python3

import sys
import base64
from Crypto.Util.number import *

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")

ords = [81, 64, 75, 66, 70, 93, 73, 72, 1, 92, 109, 2, 84, 109, 66, 75, 70, 90, 2, 92, 79]

# ---------------------------------------------------------------------------------------------------------
print("Here is your flag:")
print("".join(chr(o ^ 0x32) for o in ords))

nums = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

print("here is your next flag")
print("".join(chr(o) for o in nums))

hex = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"

# ---------------------------------------------------------------------------------------------------------
print("the bytes are: ")
print(bytes.fromhex(hex))

# ---------------------------------------------------------------------------------------------------------
hex = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
byts = bytes.fromhex(hex)
b64_str = base64.b64encode(byts)
print("base64 encoded string is")
print(b64_str)

# ---------------------------------------------------------------------------------------------------------
bigint =  11515195063862318899931685488813747395775516287289682636499965282714637259206269 
print("converting the big integer back into a message")
print(long_to_bytes(bigint))

str = "label"
result = ""

for c in str:
    res = ord(c) ^ 13
    result += chr(res)

print("the XORed string is:", result)

# ---------------------------------------------------------------------------------------------------------
def xor_truncate_after_short_string(b1, b2):
    # xor byte by byte upto the length of the shortest byte string.
    return bytes([a ^ b for a, b in zip(b1, b2)])

key1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
key23 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
byts_key1 = bytes.fromhex(key1)
byts_key23 = bytes.fromhex(key23)
res_byts = xor_truncate_after_short_string(byts_key1, byts_key23)
flag_res_byts = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"
flag = xor_truncate_after_short_string(res_byts , bytes.fromhex(flag_res_byts))
print("the flag is", flag)

# ---------------------------------------------------------------------------------------------------------
# generate all possible byte values for a single byte.
all_bytes = range(256)

def xor_with_single_byte(b, sb):
    return bytes([b ^ byt for byt in sb])

result = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

#for byte in all_bytes:
    # since the encryption is done with a single byte.
    # print(xor_with_single_byte(byte, bytes.fromhex(result)))

# ---------------------------------------------------------------------------------------------------------
result = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
print(bytes.fromhex(result))

i = 0
print(bytes([a ^ b for a, b in zip(b'crypto{', bytes.fromhex(result))]))
print(xor_truncate_after_short_string(b'{', b'04'))
print(xor_with_single_byte(ord('_'), bytes.fromhex("342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")))

# the print shows that the key begins with 'myXORke', just add y.
print(len(bytes.fromhex(result)))

partial_key = b'myXORkey'
cipher_bytes = bytes.fromhex(result)

# Since the key repeats, we extend it to match the length of the ciphertext
key = (partial_key * (len(cipher_bytes) // len(partial_key) + 1))[:len(cipher_bytes)]

# Decrypt the full ciphertext by XORing it with the key
decrypted_bytes = bytes([cipher_bytes[i] ^ key[i] for i in range(len(cipher_bytes))])
print(decrypted_bytes)
print(xor_truncate_after_short_string(b'myXORkey', bytes.fromhex(result)))
