import streamlit as st
import hashlib

st.title("Hashing Algorithms")

text = st.text_input("Enter text to hash")
algorithm = st.selectbox("Select algorithm", ["MD5", "SHA-1", "SHA-256", "SHA-512"])

if st.button("Hash"):
    if not text.strip():
        st.error("Please enter text to hash.")
    else:
        try:
            if algorithm == "MD5":
                result = hashlib.md5(text.encode()).hexdigest()
            elif algorithm == "SHA-1":
                result = hashlib.sha1(text.encode()).hexdigest()
            elif algorithm == "SHA-256":
                result = hashlib.sha256(text.encode()).hexdigest()
            elif algorithm == "SHA-512":
                result = hashlib.sha512(text.encode()).hexdigest()

            st.success("Hashed Result:")
            st.code(result)
        except Exception as e:
            st.error(f"Error: {e}")
