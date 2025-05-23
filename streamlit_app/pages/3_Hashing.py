import streamlit as st
import hashlib

st.title("🧾 Hashing Algorithms")

st.markdown("""
Hash your message using secure hash functions.

- Hashes are **one-way** and cannot be decrypted.
- Useful for data integrity, password storage, etc.
""")

text = st.text_input("Text to Hash", help="Type the message you want to hash.")
algorithm = st.selectbox("Select Hashing Algorithm", ["MD5", "SHA-1", "SHA-256", "SHA-512"], help="Choose the hashing function.")

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

# File Hashing section
st.markdown("---")
st.subheader("File Hashing")

uploaded_file = st.file_uploader("Upload a file to hash", type=None, key="file_hash")

if uploaded_file:
    file_bytes = uploaded_file.read()
    file_algo = st.selectbox("Select Hashing Algorithm for File", ["MD5", "SHA-1", "SHA-256", "SHA-512"], key="file_algo")

    if st.button("Hash File"):
        try:
            if file_algo == "MD5":
                result = hashlib.md5(file_bytes).hexdigest()
            elif file_algo == "SHA-1":
                result = hashlib.sha1(file_bytes).hexdigest()
            elif file_algo == "SHA-256":
                result = hashlib.sha256(file_bytes).hexdigest()
            elif file_algo == "SHA-512":
                result = hashlib.sha512(file_bytes).hexdigest()

            st.success("File Hash:")
            st.code(result)
        except Exception as e:
            st.error(f"Hashing Error: {e}")
