from flask import Flask, request, jsonify
from challenge import Encryption_Challenge, Decryption_Solution
import secret

app = Flask(__name__)

@app.route('/poly', methods=['GET'])
def poly():
    enc = Encryption_Challenge(256, 30)
    return jsonify(enc.get_key_poly(int(request.args.get('x'))))

@app.route('/ciphertext', methods=['GET'])
def ciphertext():
    enc = Encryption_Challenge(256, 30)
    return jsonify(enc.encrypt_flag(secret.FLAG))

@app.route('/decrypt', methods=['GET'])
def decrypt():
    dec = Decryption_Solution(request.args.get('key'), request.args.get('iv'))
    return jsonify({'cleartext': dec.decrypt_flag(request.args.get('ciphertext')).decode()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
