from flask import Flask, jsonify, request
import pandas as pd
import joblib


app = Flask(__name__)

lr = joblib.load('model.pkl')


@app.route('/predict', methods=['GET'])
def predict():
    json = request.json
    query_df = pd.DataFrame(json)
    query = pd.get_dummies(query_df)

    prediction = lr.predict(query)
    return jsonify({'prediction': list(prediction)})

