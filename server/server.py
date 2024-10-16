from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import joblib

app = Flask(__name__)

# Enable CORS
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
@cross_origin()
def home():
    return "Let's build a flight delay prediction api!"


# Load the model from the file
model = joblib.load('model.pkl')


@app.route('/predict', methods=['GET'])
@cross_origin()
def predict():
    try:
        # Extract query parameters
        day_of_week = int(request.args.get('day_of_week'))
        airport_id = int(request.args.get('airport_id'))
    except (TypeError, ValueError):
        return jsonify({'error': 'Invalid input. Please provide integers for day_of_week and airport_id.'}), 400

    # Prepare input features for the model
    input_features = [[day_of_week, airport_id]]

    # Predict probabilities
    proba = model.predict_proba(input_features)[0]
    proba_list = proba.tolist()
    not_delayed_prob = float(proba_list[0])
    delayed_prob = float(proba_list[1])

    # Convert to percentage
    confidence_percent = round(not_delayed_prob * 100)
    delayed_percent = round(delayed_prob * 100)

    # Determine delay sentence
    if delayed_prob > not_delayed_prob:
        message = "The flight is likely to be delayed."
    else:
        message = "The flight is unlikely to be delayed."

    # Prepare response
    response = {
        'prediction': proba_list,
        'confidence_percent': confidence_percent,
        'delayed_percent': delayed_percent,
        'message': message
    }

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
