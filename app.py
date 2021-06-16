import  re
from    flask           import Flask, render_template, request, redirect
from    flask.helpers   import url_for
from numpy.core.numeric import outer
import  model_prediction

app = Flask(__name__)



# @app.route()
# def home(): 
#     output = request.args.get('output', None)
#     return render_template('index.html', output = output)


@app.route('/', methods= ['POST', 'GET'])
def processed_data():
    if request.method == 'POST':
        name        = request.form.get('name', "")
        age         = request.form.get('age')
        sex         = request.form.get('sex')
        cp          = request.form.get('cp')
        trtbs       = request.form.get('trtbs')
        chol        = request.form.get('chol')
        fbs         = request.form.get('fbs')
        restEcg     = request.form.get('rest_ecg', '0')
        thalanch    = request.form.get('thalanch')
        exang       = request.form.get('exang')
        l = [age, sex,cp, trtbs, chol, fbs, restEcg, thalanch, exang]
        print(l)
        output = model_prediction.prediction(l)
        return render_template('heart.html', output= output)

    return render_template('index.html')


if __name__=='__main__':
    app.run(debug=True)