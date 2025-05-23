import streamlit as st
from algorithms.rsa import generate_rsa_key_pair, rsa_encrypt, rsa_decrypt
from algorithms.ecies import generate_ecies_key_pair, ecies_encrypt, ecies_decrypt

st.title("Asymmetric Encryption")

algorithm = st.selectbox("Select Algorithm", ["RSA", "ECIES"])
text = st.text_input("Text to Encrypt or Decrypt", key="text_input")
operation = st.selectbox("Operation", ["Encrypt", "Decrypt"])

# Initialize session state if not already present
st.session_state.setdefault("rsa_pub", "")
st.session_state.setdefault("rsa_priv", "")
st.session_state.setdefault("ecies_pub", "")
st.session_state.setdefault("ecies_priv", "")

if algorithm == "RSA":
    if st.button("Generate Key Pair"):
        pub, priv = generate_rsa_key_pair()
        st.session_state["rsa_pub"] = pub
        st.session_state["rsa_priv"] = priv
        st.success("RSA key pair generated and populated.")

    col1, col2 = st.columns(2)
    with col1:
        st.text_area("Public Key (PEM)", value=st.session_state["rsa_pub"], key="rsa_pub", height=150)
    with col2:
        st.text_area("Private Key (PEM)", value=st.session_state["rsa_priv"], key="rsa_priv", height=150)

    if st.button("Submit RSA"):
        if not text.strip() or (operation == "Encrypt" and not st.session_state.rsa_pub.strip()) or (operation == "Decrypt" and not st.session_state.rsa_priv.strip()):
            st.error("Text and the appropriate RSA key must be provided.")
        else:
            try:
                result = rsa_encrypt(text, st.session_state.rsa_pub) if operation == "Encrypt" else rsa_decrypt(text, st.session_state.rsa_priv)
                st.success("Result:")
                st.code(result)
            except Exception as e:
                st.error(f"Error: {e}")

elif algorithm == "ECIES":
    if st.button("Generate Key Pair (ECIES)"):
        pub, priv = generate_ecies_key_pair()
        st.session_state.ecies_pub = pub
        st.session_state.ecies_priv = priv
        st.success("ECIES key pair generated and populated.")

    col1, col2 = st.columns(2)
    with col1:
        st.text_input("Public Key (hex)", value=st.session_state.ecies_pub, key="ecies_pub")
    with col2:
        st.text_input("Private Key (hex)", value=st.session_state.ecies_priv, key="ecies_priv")

    if st.button("Submit ECIES"):
        if not text.strip() or (operation == "Encrypt" and not st.session_state.ecies_pub.strip()) or (operation == "Decrypt" and not st.session_state.ecies_priv.strip()):
            st.error("Text and the appropriate ECIES key must be provided.")
        else:
            try:
                result = ecies_encrypt(text, st.session_state.ecies_pub) if operation == "Encrypt" else ecies_decrypt(text, st.session_state.ecies_priv)
                st.success("Result:")
                st.code(result)
            except Exception as e:
                st.error(f"Error: {e}")
