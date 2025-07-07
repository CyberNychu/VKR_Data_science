import numpy as np
import flask
from flask import Flask, render_template
import pickle


app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['POST','GET'])


@app.route('/index', methods=['POST','GET'])
def main():
    if flask.request.method == 'GET':
        return render_template('main.html')
    
    if flask.request.method == 'POST':
        with open('model_smn.pkl', "rb") as file:
            model_smn = pickle.load(file)

        x_1 = float(flask.request.form['plot'])
        x_2 = float(flask.request.form['m_uprg'])
        x_3 = float(flask.request.form['otv'])
        x_4 = float(flask.request.form['popv'])
        x_5 = float(flask.request.form['mupr'])
        x_6 = float(flask.request.form['pr_ras'])
        x_7 = float(flask.request.form['s_nash'])
        x_8 = float(flask.request.form['pl_nash'])
        x_9 = float(flask.request.form['ug_0'])
        x_10 = float(flask.request.form['ug_90'])
        x_11 = float(flask.request.form['seg'])
        x_12 = float(flask.request.form['psmol'])
        spisok = np.array([[x_1, x_2, x_3,x_4,x_5,x_6,x_7,x_8,x_9,x_10,x_11,x_12,]])
        y_predict = model_smn.predict(spisok)

        return render_template('main.html', result = y_predict)

if __name__ == '__main__':
    app.run(debug=True)