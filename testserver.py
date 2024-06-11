from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

RECAPTCHA_SECRET_KEY = '6LdKSPYpAAAAAJrtV3ydw3Pkk5UlzwyhJ-MiGdFs'  # Replace with your actual reCAPTCHA secret key

@app.route('/verify-recaptcha', methods=['POST'])
def verify_recaptcha():
    response_token = request.form.get('g-recaptcha-response')
    remote_ip = request.remote_addr

    if not response_token:
        return jsonify({'success': False, 'error': 'missing-input-response'}), 400

    # Verify the response token with Google reCAPTCHA API
    verification_response = requests.post(
        'https://www.google.com/recaptcha/api/siteverify',
        data={
            'secret': RECAPTCHA_SECRET_KEY,
            'response': response_token,
            'remoteip': remote_ip
        }
    )

    verification_result = verification_response.json()

    if verification_result.get('success'):
        return jsonify({'success': True}), 200
    else:
        return jsonify({'success': False, 'error-codes': verification_result.get('error-codes')}), 400

if __name__ == '__main__':
    app.run(debug=True)
