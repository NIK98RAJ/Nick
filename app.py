from flask import Flask, render_template, request, jsonify
import requests

import os

app = Flask(__name__)

API_URL = "https://frontend-production-2a34.up.railway.app/api/v1/prediction/15569589-8b42-461e-89a3-f7cd3e055251"

@app.route('/')
def home():
    print(os.getcwd())
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.form.get('message')
    payload = {"question": message}
    response = requests.post(API_URL, json=payload)


    return response.text

if __name__ == "__main__":
    app.run(debug=True)
