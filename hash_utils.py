import hashlib

def hash_text(text, algorithm):
    h = getattr(hashlib, algorithm)()
    h.update(text.encode())
    return h.hexdigest()
