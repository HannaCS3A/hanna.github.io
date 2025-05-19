from flask import Flask, render_template, request
from algorithms.aes import encrypt_text, decrypt_text  # Correctly imported functions
from algorithms.rsa_encrypt import encrypt_text as rsa_encrypt_text, decrypt_text as rsa_decrypt_text
from algorithms.hash_utils import hash_text
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'AC_FP'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/symmetric', methods=['GET', 'POST'])
def symmetric():
    result = ""
    if request.method == 'POST':
        text = request.form.get('text')
        key = request.form.get('key')
        operation = request.form.get('operation')

        if operation == 'encrypt':
            result = encrypt_text(text, key)  # Correct function call
        elif operation == 'decrypt':
            result = decrypt_text(text, key)  # Correct function call
    return render_template('symmetric.html', result=result)

@app.route('/asymmetric', methods=['GET', 'POST'])
def asymmetric():
    result = ""
    if request.method == 'POST':
        text = request.form.get('text')
        operation = request.form.get('operation')

        if operation == 'encrypt':
            result = rsa_encrypt_text(text)  # Correct function call (using alias)
        elif operation == 'decrypt':
            ciphertext = request.form.get('text')
            result = rsa_decrypt_text(ciphertext)  # Correct function call (using alias)
    return render_template('asymmetric.html', result=result)

@app.route('/hash', methods=['GET', 'POST'])
def hash_text_route():  # Renamed function to avoid collision with imported function
    result = ""
    if request.method == 'POST':
        text = request.form.get('text')
        algorithm = request.form.get('algorithm')
        result = hash_text(text, algorithm)  # Correct function call
    return render_template('hash.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
