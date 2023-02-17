import traceback
from flask import Flask, jsonify, request
import pandas as pd
import joblib


app = Flask(__name__)

lr = joblib.load('model.pkl')
model_columns = joblib.load('model_columns.pkl')


@app.route('/predict', methods=['GET'])
def predict():
    if lr:
        try:
            json = request.json
            query = pd.get_dummies(pd.DataFrame(json))
            query = query.reindex(columns=model_columns, fill_value=0)

            prediction = lr.predict(query)
            return jsonify({'prediction': list(prediction)})
        except:
            return jsonify({'trace': traceback.format_exc()})
    else:
        print('Train the model first')
        return ('No model here to use')

