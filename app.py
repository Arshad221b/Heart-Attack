import re
from flask import Flask, render_template, request, redirect
import model_prediction

app = Flask(__name__)

@app.route('/')
def home(): 
    return render_template('home.html')

@app.route('/', methods= ['POST'])
def processed_data():
    name        = request.form['name']
    age         = request.form['age']
    sex         = request.form['sex']
    exang       = request.form['exang']
    ca          = request.form['ca']
    cp          = request.form['cp']
    trtbs       = request.form['trtbs']
    chol        = request.form['chol']
    fbs         = request.form['fbs']
    restEcg     = request.form['rest_ecg']
    thalanch    = request.form['thalanch']
    l = [age, sex, exang, ca, cp, trtbs, chol, fbs, restEcg, thalanch]
    output = model_prediction.prediction(l)
    return redirect('heart.html', output= output)


if __name__=='__main__':
    app.run(debug=True)