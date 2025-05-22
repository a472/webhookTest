from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Received data:", data)
    return {'status': 'success'}, 200

@app.route('/', methods=['GET'])
def home():
    return "Webhook is running!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
  
