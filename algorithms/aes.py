from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def encrypt_text(text, key):
    key = key.encode('utf-8')
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(text.encode('utf-8'), AES.block_size))
    iv = cipher.iv
    return iv.hex() + ct_bytes.hex()

def decrypt_text(encrypted_text, key):
    encrypted_text = bytes.fromhex(encrypted_text)
    iv = encrypted_text[:16]
    ct = encrypted_text[16:]
    key = key.encode('utf-8')
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(ct), AES.block_size)
    return decrypted.decode('utf-8')
