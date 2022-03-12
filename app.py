from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')



@app.route("/predict", methods=['POST'])
def predict():
    Florida=0
    if request.method == 'POST':
        RD_Spend = float(request.form['R&D_Spend'])
        Administration=float(request.form['Administration'])
        Marketing_Spend=float(request.form['Marketing_Spend'])
        State=request.form['State']
        if(State=='NewYork'):
            NewYork=1
            Florida=0
        elif(State=="Florida"):
            NewYork=0
            Florida=1 
        else:
            NewYork=0
            Florida=0 
        prediction=model.predict([[RD_Spend,Administration,Marketing_Spend,Florida,NewYork]])
        output=round(prediction[0],2)
        if output<0:
             return render_template('index.html',prediction_texts="Bleh")
        else:
             return render_template('index.html',prediction_text="The profit is {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
