# create a basic server using Flask
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


@app.route('/predict', methods=['GET'])
@cross_origin()
def predict_delay():
    # Extract query parameters
    day_of_week = request.args.get('day_of_week')
    airport_id = request.args.get('airport_id')
    
    # Validate parameters
    if day_of_week is None or airport_id is None:
        return jsonify({"error": "Missing parameters"}), 400
    
    try:
        day_of_week = int(day_of_week)
        airport_id = int(airport_id)
    except ValueError:
        return jsonify({"error": "Invalid parameter types"}), 400

    # Prepare input for the model
    input_features = [[day_of_week, airport_id]]
    
    # Predict probabilities
    prediction_proba = model.predict_proba(input_features)[0]
    prob_not_delayed = prediction_proba[0] * 100
    prob_delayed = prediction_proba[1] * 100
    
    # Convert to percentages with zero decimal places
    confidence_percent = round(prob_not_delayed)
    delayed_percent = round(prob_delayed)
    
    # Determine prediction
    if prob_delayed > prob_not_delayed:
        sentence = "The flight will be delayed."
        model_prediction = "Delayed"
    else:
        sentence = "The flight will not be delayed."
        model_prediction = "Not Delayed"
    
    # Create response
    response = {
        "model_prediction": model_prediction,
        "confidence_percent": confidence_percent,
        "delayed_percent": delayed_percent,
        "sentence": sentence
    }
    
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
