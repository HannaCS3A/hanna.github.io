def caesar_encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted += char
    return encrypted

def caesar_decrypt(ciphertext, shift):
    return caesar_encrypt(ciphertext, -shift)

def xor_encrypt(text, key):
    encrypted_bytes = bytes([b ^ key for b in text.encode('utf-8')])
    return encrypted_bytes.hex()

def xor_decrypt(ciphertext, key):
    try:
        encrypted_bytes = bytes.fromhex(ciphertext)
        decrypted_bytes = bytes([b ^ key for b in encrypted_bytes])
        return decrypted_bytes.decode('utf-8')
    except Exception as e:
        raise ValueError("Invalid XOR ciphertext or key.") from e