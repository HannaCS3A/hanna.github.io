import base64
import hashlib
from Crypto.Cipher import AES
import os

# for file encryption on AES, Caesar, and XOR Ciphers

def pad(text):
    return text + b' ' * (16 - len(text) % 16)

def get_aes_key(key):
    return hashlib.sha256(key.encode()).digest()

def aes_encrypt_file(file_bytes, key):
    cipher = AES.new(get_aes_key(key), AES.MODE_ECB)
    padded = pad(file_bytes)
    encrypted = cipher.encrypt(padded)
    return base64.b64encode(encrypted)

def aes_decrypt_file(file_bytes, key):
    cipher = AES.new(get_aes_key(key), AES.MODE_ECB)
    decrypted = cipher.decrypt(base64.b64decode(file_bytes))
    return decrypted.rstrip(b' ')

def caesar_encrypt_file(file_bytes, shift):
    return bytes([(b + shift) % 256 for b in file_bytes])

def caesar_decrypt_file(file_bytes, shift):
    return bytes([(b - shift) % 256 for b in file_bytes])

def xor_encrypt_file(file_bytes, key):
    return bytes([b ^ key for b in file_bytes])

xor_decrypt_file = xor_encrypt_file