from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os


def generate_ecies_key_pair():
    private_key = ec.generate_private_key(ec.SECP256R1(), default_backend())
    public_key = private_key.public_key()

    private_bytes = private_key.private_numbers().private_value.to_bytes(32, byteorder='big')
    public_bytes = public_key.public_bytes(
        serialization.Encoding.X962,
        serialization.PublicFormat.UncompressedPoint
    )

    return public_bytes.hex(), private_bytes.hex()


def ecies_encrypt(plaintext, pub_hex):
    try:
        pub_hex = pub_hex.strip()
        pub_bytes = bytes.fromhex(pub_hex)
        public_key = ec.EllipticCurvePublicKey.from_encoded_point(ec.SECP256R1(), pub_bytes)

        ephemeral_key = ec.generate_private_key(ec.SECP256R1(), default_backend())
        shared_key = ephemeral_key.exchange(ec.ECDH(), public_key)

        derived_key = HKDF(
            algorithm=hashes.SHA256(),
            length=32,
            salt=None,
            info=b'ecies-encryption',
            backend=default_backend()
        ).derive(shared_key)

        iv = os.urandom(12)
        encryptor = Cipher(
            algorithms.AES(derived_key),
            modes.GCM(iv),
            backend=default_backend()
        ).encryptor()

        ciphertext = encryptor.update(plaintext.encode()) + encryptor.finalize()
        tag = encryptor.tag

        ephemeral_pub = ephemeral_key.public_key().public_bytes(
            serialization.Encoding.X962,
            serialization.PublicFormat.UncompressedPoint
        )

        return (ephemeral_pub + iv + tag + ciphertext).hex()

    except ValueError as e:
        raise ValueError(f"Invalid public key format: {e}")


def ecies_decrypt(ciphertext_hex, priv_hex):
    try:
        priv_hex = priv_hex.strip()
        priv_bytes = bytes.fromhex(priv_hex)
        ciphertext_bytes = bytes.fromhex(ciphertext_hex)

        private_value = int.from_bytes(priv_bytes, byteorder='big')
        private_key = ec.derive_private_key(private_value, ec.SECP256R1(), default_backend())

        ephemeral_pub = ciphertext_bytes[:65]
        iv = ciphertext_bytes[65:77]
        tag = ciphertext_bytes[77:93]
        actual_ciphertext = ciphertext_bytes[93:]

        ephemeral_public_key = ec.EllipticCurvePublicKey.from_encoded_point(ec.SECP256R1(), ephemeral_pub)
        shared_key = private_key.exchange(ec.ECDH(), ephemeral_public_key)

        derived_key = HKDF(
            algorithm=hashes.SHA256(),
            length=32,
            salt=None,
            info=b'ecies-encryption',
            backend=default_backend()
        ).derive(shared_key)

        decryptor = Cipher(
            algorithms.AES(derived_key),
            modes.GCM(iv, tag),
            backend=default_backend()
        ).decryptor()

        plaintext = decryptor.update(actual_ciphertext) + decryptor.finalize()
        return plaintext.decode()

    except ValueError as e:
        raise ValueError(f"Invalid key or ciphertext format: {e}")
    except Exception as e:
        raise Exception(f"Decryption failed: {e}")
