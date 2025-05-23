import streamlit as st
from algorithms.aes import aes_encrypt, aes_decrypt

st.title("Symmetric Encryption - AES")

text = st.text_input("Enter text to encrypt or decrypt")
operation = st.radio("Operation", ["Encrypt", "Decrypt"])
key = st.text_input("Key")

if st.button("Submit"):
    if not text.strip() or not key.strip():
        st.error("Both text and key must be provided.")
    else:
        try:
            result = aes_encrypt(text, key) if operation == "Encrypt" else aes_decrypt(text, key)
            st.success("Result:")
            st.code(result)
        except Exception as e:
            st.error(f"Error: {e}")
