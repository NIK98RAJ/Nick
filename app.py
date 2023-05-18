from flask import Flask, render_template, request, jsonify
import requests

import os

app = Flask(__name__)

API_URL = "https://frontend-production-2a34.up.railway.app/api/v1/prediction/3fe0d972-94da-4d74-86f9-b4e9aaa3cae3"

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
