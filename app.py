import json
from flask import Flask, request, app, jsonify, url_for, render_template
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)
xgmodel = pickle.load(open('xgbmodel.pkl', 'rb'))

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data=request.json['data']
    data = {k:[v] for k,v in data.items()}
    data2 = pd.DataFrame.from_dict(data)
    output=xgmodel.predict(data2)
    return str(output)

@app.route('/predict', methods=['POST'])
def predict():
  data=[float(x) for x in request.form.values()]
  data2 = pd.DataFrame(data).T
  output = xgmodel.predict(data2)
  return render_template("home.html", prediction_text=f'The prediction of this transaction being fraud is {bool(output)} according to the model.')

if __name__ == '__main__':
  app.run(debug=True)