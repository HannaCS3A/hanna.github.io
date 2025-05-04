from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

key = RSA.generate(2048)
public_key = key.publickey()
encryptor = PKCS1_OAEP.new(public_key)
decryptor = PKCS1_OAEP.new(key)

def encrypt_text(text):
    encrypted = encryptor.encrypt(text.encode())
    return base64.b64encode(encrypted).decode()

def decrypt_text(ciphertext):
    decrypted = decryptor.decrypt(base64.b64decode(ciphertext))
    return decrypted.decode()
