from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
import hashlib

def pad(text):
    while len(text) % 16 != 0:
        text += ' '
    return text

def get_aes_key(key):
    return hashlib.sha256(key.encode()).digest()

def aes_encrypt(plaintext, key):
    key_bytes = get_aes_key(key)
    cipher = AES.new(key_bytes, AES.MODE_ECB)
    padded_text = pad(plaintext)
    ciphertext = cipher.encrypt(padded_text.encode())
    return base64.b64encode(ciphertext).decode()

def aes_decrypt(ciphertext, key):
    key_bytes = get_aes_key(key)
    cipher = AES.new(key_bytes, AES.MODE_ECB)
    decoded = base64.b64decode(ciphertext)
    decrypted = cipher.decrypt(decoded).decode()
    return decrypted.strip()
