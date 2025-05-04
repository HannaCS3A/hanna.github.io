from Crypto.Cipher import AES
import base64
from Crypto.Util.Padding import pad, unpad

def encrypt_text(text, key):
    key = key.ljust(16)[:16].encode()
    cipher = AES.new(key, AES.MODE_ECB)
    ct_bytes = cipher.encrypt(pad(text.encode(), AES.block_size))
    return base64.b64encode(ct_bytes).decode()

def decrypt_text(ciphertext, key):
    key = key.ljust(16)[:16].encode()
    cipher = AES.new(key, AES.MODE_ECB)
    ct_bytes = base64.b64decode(ciphertext)
    return unpad(cipher.decrypt(ct_bytes), AES.block_size).decode()
