from flask import Flask, render_template, request, jsonify
from algorithms.aes import encrypt_text, decrypt_text  
from algorithms.rsa_encrypt import encrypt_text as rsa_encrypt_text, decrypt_text as rsa_decrypt_text, generate_keys
from algorithms.hash_utils import hash_text
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'AC_FP'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/generate_keys', methods=['GET'])
def generate_keys_route():
    private_key, public_key = generate_keys()
    return jsonify({
        'public_key': public_key.decode(),
        'private_key': private_key.decode()
    })

@app.route('/symmetric', methods=['GET', 'POST'])
def symmetric():
    result = ""
    if request.method == 'POST':
        text = request.form.get('text')
        key = request.form.get('key')
        operation = request.form.get('operation')

        if operation == 'encrypt':
            result = encrypt_text(text, key)  
        elif operation == 'decrypt':
            result = decrypt_text(text, key) 
    return render_template('symmetric.html', result=result)

@app.route('/asymmetric', methods=['GET', 'POST'])
def asymmetric():
    result = ""
    if request.method == 'POST':
        text = request.form.get('text')
        operation = request.form.get('operation')
        public_key = request.form.get('public_key')
        private_key = request.form.get('private_key')

        try:
            if operation == 'encrypt' and public_key:
                result = rsa_encrypt_text(text, public_key)
            elif operation == 'decrypt' and private_key:
                result = rsa_decrypt_text(text, private_key)
            else:
                result = "Missing required key input."
        except ValueError as ve:
            result = f"Key error: {str(ve)}"
        except Exception as e:
            result = f"Unexpected error: {str(e)}"

    return render_template('asymmetric.html', result=result)


@app.route('/hash', methods=['GET', 'POST'])
def hash_text_route():
    result = ""
    if request.method == 'POST':
        text = request.form.get('text')
        algorithm = request.form.get('algorithm')
        result = hash_text(text, algorithm) 
    return render_template('hash.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
