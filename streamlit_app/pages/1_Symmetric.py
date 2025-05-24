import streamlit as st
from algorithms.aes import aes_encrypt, aes_decrypt
from algorithms.caesar_xor import caesar_encrypt, caesar_decrypt, xor_encrypt, xor_decrypt
from algorithms.file_symmetric import (
    aes_encrypt_file, aes_decrypt_file,
    caesar_encrypt_file, caesar_decrypt_file,
    xor_encrypt_file, xor_decrypt_file
)

st.title("🔒 Symmetric Encryption")

st.markdown("""
Choose a symmetric encryption algorithm to encrypt or decrypt your text:

- **AES (Advanced Encryption Standard)**: Secure industry-standard algorithm using a secret key.
- **Caesar Cipher**: Simple substitution cipher with a numeric shift.
- **XOR Cipher**: Basic encryption using a byte-sized numeric key.
""")

algorithm = st.selectbox("Select Symmetric Algorithm", ["AES", "Caesar Cipher", "XOR Cipher"])
text = st.text_input("Text to Encrypt or Decrypt", help="Enter the plain or encrypted text here.")
operation = st.selectbox("Operation", ["Encrypt", "Decrypt"], help="Choose whether to encrypt or decrypt the input.")

# AES section
if algorithm == "AES":
    key = st.text_input("Key (Secret)", type="password", help="Enter a passphrase to be hashed as AES key.")
    if st.button(operation, key="aes_text_op"):
        if not text.strip() or not key.strip():
            st.error("Text and key must be provided.")
        else:
            try:
                result = aes_encrypt(text, key) if operation == "Encrypt" else aes_decrypt(text, key)
                st.success("Result:")
                st.code(result)
            except Exception as e:
                st.error(f"Error: {e}")

# Caesar Cipher section
elif algorithm == "Caesar Cipher":
    shift = st.number_input("Shift Value", step=1, format="%d", help="Enter the number of positions to shift.")
    if st.button(operation, key="caesar_text_op"):
        if not text.strip():
            st.error("Text input is required.")
        else:
            try:
                shift_val = int(shift)
                result = caesar_encrypt(text, shift_val) if operation == "Encrypt" else caesar_decrypt(text, shift_val)
                st.success("Result:")
                st.code(result)
            except Exception as e:
                st.error(f"Error: {e}")

# XOR Cipher section
elif algorithm == "XOR Cipher":
    key = st.number_input("Byte Key (0-255)", min_value=0, max_value=255, step=1, help="Enter a byte value to XOR with the text.")
    if st.button(operation, key="xor_text_op"):
        if not text.strip():
            st.error("Text input is required.")
        else:
            try:
                key_val = int(key)
                result = xor_encrypt(text, key_val) if operation == "Encrypt" else xor_decrypt(text, key_val)
                st.success("Result:")
                st.code(result)
            except Exception as e:
                st.error(f"Error: {e}")

# File Encryption section
st.markdown("---")
st.subheader("File Encryption/Decryption")

uploaded_file = st.file_uploader("Choose a file to encrypt or decrypt")
file_operation = st.selectbox("File Operation", ["Encrypt", "Decrypt"])
file_key_input = ""

if algorithm == "AES":
    file_key_input = st.text_input("File Key (AES)", type="password", key="file_aes_key")
elif algorithm == "Caesar Cipher":
    file_key_input = st.number_input("Shift Value (Caesar)", key="file_caesar_key", step=1, format="%d")
elif algorithm == "XOR Cipher":
    file_key_input = st.number_input("Byte Key (XOR)", min_value=0, max_value=255, step=1, key="file_xor_key")

# Fix duplicate ID error by assigning a unique key
if st.button(file_operation, key=f"{algorithm}_{file_operation}_file_op"):
    if uploaded_file is None:
        st.error("Please upload a file to encrypt or decrypt.")
    else:
        file_bytes = uploaded_file.read()

        try:
            if algorithm == "AES":
                if not file_key_input.strip():
                    st.error("Please enter a key.")
                else:
                    result_bytes = aes_encrypt_file(file_bytes, file_key_input) if file_operation == "Encrypt" else aes_decrypt_file(file_bytes, file_key_input)

            elif algorithm == "Caesar Cipher":
                result_bytes = caesar_encrypt_file(file_bytes, int(file_key_input)) if file_operation == "Encrypt" else caesar_decrypt_file(file_bytes, int(file_key_input))

            elif algorithm == "XOR Cipher":
                result_bytes = xor_encrypt_file(file_bytes, int(file_key_input))

            st.success("File processed successfully.")
            st.download_button("Download Result", result_bytes, file_name=f"processed_{uploaded_file.name}")
        except Exception as e:
            st.error(f"Error: {e}")
