from flask import Flask, escape, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.route('/')
def welcome():
    return "<h1 style='text-align: center'>ECOMMERCE API</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)