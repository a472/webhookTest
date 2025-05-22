from flask import Flask, request
import os

app = Flask(__name__)

VERIFY_TOKEN = "my_secret_token_4561"

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    print("Received webhook request")  # Add logging
    if request.method == 'GET':
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        print(f"Token: {token}, Challenge: {challenge}")  # Add logging
        if token == VERIFY_TOKEN:
            return str(challenge), 200
        return "Verification token mismatch", 403

    print(request.json)
    return "OK", 200

@app.route('/', methods=['GET'])
def home():
    return "Server is running!", 200

# Railway will set the PORT environment variable
port = int(os.environ.get("PORT", 8080))
app.run(host='0.0.0.0', port=port)
