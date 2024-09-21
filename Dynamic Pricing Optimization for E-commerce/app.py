from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict_price', methods=['POST'])
def predict_price():
    data = request.get_json()
    features = [data['features']]  # Assuming the features are correctly passed in the POST request.
    price_pred = rf_model.predict(features)  # Make sure rf_model is defined and loaded before use.
    return jsonify({'optimal_price': price_pred[0]})

if __name__ == '__main__':
    app.run(debug=True)
