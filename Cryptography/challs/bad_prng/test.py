import random
import string
import time
from base64 import b64encode
from Crypto.Cipher import AES

"""
Generates a random key
"""


def random_key(size: int) -> string:
    return ''.join(random.choice(string.ascii_letters) for x in range(size)).encode("utf-8")


t = int(time.time())
random.seed(t)
key = random_key(16)
data = b""  # secret
cipher = AES.new(key, AES.MODE_CTR)
encrypted_data = cipher.encrypt(data)
print("Flag is  :", b64encode(encrypted_data).decode("utf-8"))
print("Nonce is :", b64encode(cipher.nonce).decode("utf-8"))

# Encrypted Flag is  : wzQY5diwciLfRQUEi3dxfzAOvR5Z2RhWXnU6HE0=
# The flag begins with YCTF
# Nonce is : x86qMt0PvIM=
# The server was running between 20h and 22h the  07 november of 2021
