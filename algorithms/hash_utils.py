import hashlib

def hash_text(text, algorithm='sha256'):
    hash_func = getattr(hashlib, algorithm, hashlib.sha256)
    hashed = hash_func(text.encode('utf-8')).hexdigest()
    return hashed
