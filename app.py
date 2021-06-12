import re
from flask import Flask, render_template, request, redirect
from flask.helpers import url_for
import model_prediction

app = Flask(__name__)

@app.route('/')
def home(): 
    return render_template('home.html')

@app.route('/heart', methods= ['POST', 'GET'])
def processed_data():
    if request.method == 'POST':
        name        = request.form.get('name', "")
        age         = request.form.get('age')
        sex         = request.form.get('sex')
        exang       = request.form.get('exang')
        ca          = request.form.get('ca')
        cp          = request.form.get('cp')
        trtbs       = request.form.get('trtbs')
        chol        = request.form.get('chol')
        fbs         = request.form.get('fbs')
        restEcg     = request.form.get('rest_ecg')
        thalanch    = request.form.get('thalanch')
        l = [age, sex, exang, ca, cp, trtbs, chol, fbs, restEcg, thalanch]
        output = model_prediction.prediction(l)
        return render_template('heart.html', output= output)

    else:
        return url_for('home')

if __name__=='__main__':
    app.run(debug=True)