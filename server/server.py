from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import pickle

app = Flask(__name__)

# Enable CORS
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
@cross_origin()
def home():
    return "Let's build a flight delay prediction api!"


# Load the model from the file
model = pickle.load(open('model.pkl', 'rb'))


if __name__ == '__main__':
    app.run(debug=True)
