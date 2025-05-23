import streamlit as st

st.title("🔍 Algorithm Information")

st.markdown("""
This section provides brief information about each cryptographic algorithm implemented in this app, including their **purpose**, **pseudocode**, and **common use cases**.
""")

def section(title, description, pseudocode, use_cases):
    st.subheader(title)
    st.markdown(f"**Description:**\n\n{description}")
    st.markdown(f"**Pseudocode:**\n\n```\n{pseudocode}\n```")
    st.markdown("**Use Cases:**")
    st.markdown(f"- " + "\n- ".join(use_cases))
    st.markdown("---")

# AES
section(
    "AES (Advanced Encryption Standard)",
    "AES is a symmetric block cipher standardized by NIST. It encrypts 128-bit blocks using a 128/192/256-bit key.",
    "1. Derive 128/192/256-bit key.\n2. Divide input into 128-bit blocks.\n3. Apply substitution-permutation network for multiple rounds.\n4. Return ciphertext.",
    ["Secure data storage", "TLS/SSL encryption", "Wi-Fi (WPA2) encryption"]
)

# Caesar Cipher
section(
    "Caesar Cipher",
    "A substitution cipher where each letter in the plaintext is shifted a fixed number of places down the alphabet.",
    "1. Choose a numeric shift.\n2. For each character in plaintext:\n   - Shift the character by the key.\n   - Wrap around alphabet if needed.\n3. Combine shifted characters to get ciphertext.",
    ["Historical cryptography", "Educational purposes", "Basic text obfuscation"]
)

# XOR Cipher
section(
    "XOR Cipher",
    "Applies a bitwise XOR operation between the text and a key. It is a simple symmetric encryption method.",
    "1. Convert key to byte.\n2. For each byte in the input:\n   - XOR it with the key.\n3. Return the result.",
    ["Simple file obfuscation", "Embedded system encoding", "Educational use"]
)

# RSA
section(
    "RSA (Rivest–Shamir–Adleman)",
    "An asymmetric encryption algorithm based on the difficulty of factoring large integers.",
    "1. Generate two large primes (p, q).\n2. Compute n = p*q and φ(n).\n3. Choose e (public key), compute d (private key).\n4. Encrypt: c = m^e mod n\n5. Decrypt: m = c^d mod n",
    ["Secure data exchange", "Digital signatures", "Public-key infrastructure (PKI)"]
)

# ECIES
section(
    "ECIES (Elliptic Curve Integrated Encryption Scheme)",
    "A hybrid encryption scheme using elliptic curve cryptography. It combines ECDH with symmetric encryption and MAC.",
    "1. Generate ephemeral EC key pair.\n2. Derive shared secret using recipient's public key.\n3. Use KDF to derive encryption and MAC keys.\n4. Encrypt message and compute MAC.\n5. Send ciphertext + MAC + ephemeral public key.",
    ["Secure messaging", "Mobile encryption", "IoT device security"]
)

# Hashing Algorithms
section(
    "Hashing Algorithms (MD5, SHA-1, SHA-256, SHA-512)",
    "Hashing algorithms map data of arbitrary size to fixed-size hashes. They are one-way and used for integrity checks.",
    "1. Accept input message.\n2. Break input into blocks.\n3. Process blocks through compression functions.\n4. Return fixed-size hash.",
    ["Password storage", "File integrity checks", "Blockchain"]
)
