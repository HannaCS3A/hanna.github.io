from flask import Flask, render_template, request, send_file
from algorithms import aes, rsa_encrypt, hash_utils
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
            result = aes.encrypt_text(text, key)
        elif operation == 'decrypt':
            result = aes.decrypt_text(text, key)
    return render_template('symmetric.html', result=result)

@app.route('/asymmetric', methods=['GET', 'POST'])
def asymmetric():
    result = ""
    if request.method == 'POST':
        text = request.form.get('text')
        operation = request.form.get('operation')

        if operation == 'encrypt':
            result = rsa_encrypt.encrypt_text(text)
        elif operation == 'decrypt':
            ciphertext = request.form.get('text')
            result = rsa_encrypt.decrypt_text(ciphertext)
    return render_template('asymmetric.html', result=result)

@app.route('/hash', methods=['GET', 'POST'])
def hash_text():
    result = ""
    if request.method == 'POST':
        text = request.form.get('text')
        algorithm = request.form.get('algorithm')
        result = hash_utils.hash_text(text, algorithm)
    return render_template('hash.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
