from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = "my_secret_token_456"

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        if token == VERIFY_TOKEN:
            return challenge, 200
        return "Verification token mismatch", 403

    # Handle incoming POST messages from WhatsApp here
    print(request.json)
    return "OK", 200
