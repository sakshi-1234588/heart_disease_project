from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [float(x) for x in request.form.values()]
    age, cholesterol, bp, max_heart_rate, oldpeak = features

    # NEW Corrected Simple Risk Logic:
    risk_score = 0

    if age > 60:
        risk_score += 1
    if bp > 140:
        risk_score += 1
    if cholesterol > 240:
        risk_score += 1
    if max_heart_rate < 100:
        risk_score += 1
    if oldpeak > 2:
        risk_score += 1

    # Now decide based on score
    if risk_score >= 2:
        result = 'High Risk of Heart Disease'
    else:
        result = 'Low Risk of Heart Disease'

    return render_template('index.html', prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)