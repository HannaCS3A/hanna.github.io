from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

def generate_keys():
    private_key = ec.generate_private_key(ec.SECP384R1())
    public_key = private_key.public_key()
    
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    
    return private_pem, public_pem

def ecies_encrypt_text(text, public_key_pem):
    public_key = serialization.load_pem_public_key(public_key_pem)
    private_key = ec.generate_private_key(ec.SECP384R1())
    shared_key = private_key.exchange(ec.ECDH(), public_key)

    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000
    )
    symmetric_key = kdf.derive(shared_key)
    
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(symmetric_key), modes.CFB(iv))
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(text.encode('utf-8')) + encryptor.finalize()

    return (iv + salt + ciphertext).hex()

def ecies_decrypt_text(ciphertext, private_key_pem):
    private_key = serialization.load_pem_private_key(private_key_pem, password=None)
    iv_and_salt_and_ciphertext = bytes.fromhex(ciphertext)
    
    iv = iv_and_salt_and_ciphertext[:16]
    salt = iv_and_salt_and_ciphertext[16:32]
    ciphertext = iv_and_salt_and_ciphertext[32:]

    public_key = private_key.public_key()
    shared_key = private_key.exchange(ec.ECDH(), public_key)

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000
    )
    symmetric_key = kdf.derive(shared_key)

    cipher = Cipher(algorithms.AES(symmetric_key), modes.CFB(iv))
    decryptor = cipher.decryptor()
    decrypted = decryptor.update(ciphertext) + decryptor.finalize()

    return decrypted.decode('utf-8')
