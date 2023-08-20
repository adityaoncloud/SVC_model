#This is the inference script for the give ml model to deploy it using Kserve as a serverless model on Kubeflow

import numpy as np
from flask import Flask, request, jsonify
from sklearn.svm import SVC
import joblib

app = Flask(__name__)

# Load the trained SVM model
model = joblib.load('trained_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json['data']
    data = np.array(data).reshape(1, -1)
    prediction = model.predict(data)
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

