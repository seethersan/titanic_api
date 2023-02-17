import sys
import traceback
from flask import Flask, jsonify, request
import pandas as pd
import joblib


app = Flask(__name__)


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


if __name__ == '__main__':
    try:
        port = int(sys.argv[1]) # This is for a command-line input
    except:
        port = 12345
    
    lr = joblib.load('model.pkl')
    print('Model loaded')
    model_columns = joblib.load('model_columns.pkl')
    print('Model columns loaded')
    app.run(port=port, debug=True)