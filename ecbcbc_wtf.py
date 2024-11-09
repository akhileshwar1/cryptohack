from great_snakes_35381fca29d68d8f3f25c9fa0a9026fb import xor_truncate_after_short_string
import requests

def encrypt():
    url = "http://aes.cryptohack.org/ecbcbcwtf/encrypt_flag/"
    r = requests.get(url)
    return r .json()['ciphertext']

def decrypt(ciphertext):
    url = "http://aes.cryptohack.org/ecbcbcwtf/decrypt"
    r = requests.get(url + "/" + ciphertext)
    return r.json()["plaintext"]

# idea is to decrypt via pn = pn' ^ cn-1, where cn-1 is the n-1th ciphertext block. 
def decrypt_cbc(ciphertext, plaintext):
    plain = ""
    for i in range(len(plaintext), 0, -32):
        plain_block = plaintext[max(0, i-32):i]
        cipher_block = ciphertext[max(0, i-64):(i-32)]
        xored_bytes = xor_truncate_after_short_string(bytes.fromhex(plain_block), bytes.fromhex(cipher_block))
        plain = xored_bytes.hex() + plain

    return plain

ciphertext = encrypt()
plaintext = decrypt(ciphertext)
print(bytes.fromhex(decrypt_cbc(ciphertext, plaintext)).decode('ascii'))
