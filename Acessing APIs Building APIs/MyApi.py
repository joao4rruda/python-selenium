from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Currency Rate API</h1> <p>Example URL: /api/v1/usd-eur</p>'

app.run(host='0.0.0.0')