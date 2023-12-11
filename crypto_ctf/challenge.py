from hashlib import sha256
from Crypto.Util.number import bytes_to_long, long_to_bytes
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
import os
import secret


class Encryption_Challenge:
    def __init__(self, BITS, d):
        self.d = d
        self.BITS = BITS
        self.key = secret.key
        self.coeffs = [self.key] + [bytes_to_long(os.urandom(self.BITS//8)) for _ in range(self.d)]

    def poly(self, x):
        return sum([self.coeffs[i] * x**i for i in range(self.d+1)])

    def get_key_poly(self, x):
        return {'x': x, 'y': self.poly(x)}
    
    def encrypt_flag(self, m):
        key = sha256(str(self.key).encode()).digest()
        iv = os.urandom(16)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        ct = cipher.encrypt(pad(m, 16))
        return {'iv': iv.hex(), 'ciphertext': ct.hex()}
    
class Decryption_Solution: 
    def __init__(self, key, iv) -> None:
        self.key = key
        self.iv = iv

    def decrypt_flag(self, ciphertext):
        key = sha256(str(self.key).encode()).digest()
        iv = long_to_bytes(int(self.iv, 16))
        ciphertext = long_to_bytes(int(ciphertext, 16))
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(ciphertext), 16)

if __name__ == '__main__':   

    enc = Encryption_Challenge(256, 30)
    ciphertext = enc.encrypt_flag(secret.FLAG)
    print(ciphertext)
    dec = Decryption_Solution(secret.key, ciphertext['iv'])
    cleartext = dec.decrypt_flag(ciphertext['ciphertext'])
    print(cleartext)
