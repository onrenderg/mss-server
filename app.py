from flask import Flask, jsonify
from flask_cors import CORS
import os 

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains



@app.route("/", methods=["GET"])
def home():
    return "<h2>Flask API is running. Visit <code>/products</code> to see the product list.</h2>"


# Sample product list
products = [
    {"id": 1, "name": "T-shirt", "price": 19.99},
    {"id": 2, "name": "Hoodie", "price": 39.99},
    {"id": 3, "name": "Sneakers", "price": 59.99}
]

@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(products)


port = int(os.getenv('PORT', 80))
print('Listening on port %s' % (port))
app.run(debug=False, host="0.0.0.0", port=port)
