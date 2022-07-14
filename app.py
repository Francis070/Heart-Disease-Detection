# from crypt import methods
import numpy as np;
import pandas as pd;
import matplotlib.pyplot  as plt;
from sklearn.model_selection  import train_test_split
from sklearn.linear_model  import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix
from model_code import predict_disease
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def predict():
    str_inputs = [str(x) for x in request.form.values()]
    inputs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i, val in enumerate(str_inputs):
        inputs[i] = float(val)

    print("Inputs in string", str_inputs)
    print("Inputs provided are", inputs)

    output = predict_disease(inputs)

    if output == 1:
        return render_template( 'index.html' , prediction_text = 'This person has heart disease or has potential to have one.')
    else:
        return render_template( 'index.html' , prediction_text = "This person doesn't has heart disease.")

if __name__ == "__main__":
    app.run(debug=True)
