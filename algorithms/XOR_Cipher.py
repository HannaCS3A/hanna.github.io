def xor_encrypt(text, key):
    encrypted_bytes = bytes([b ^ key for b in text.encode('utf-8')])
    return encrypted_bytes.hex()  # Return as hex string

def xor_decrypt(ciphertext, key):
    encrypted_bytes = bytes.fromhex(ciphertext)
    decrypted_bytes = bytes([b ^ key for b in encrypted_bytes])
    return decrypted_bytes.decode('utf-8')
