from flask import Flask,render_template,request
import pickle
import numpy as np
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/predict')
def predict():
    return render_template('predict.html')
@app.route('/data_predict',methods=['POST'])
def data_predict():
    Age=request.form['Age']
    Gender=request.form['Gender']
    Total_Bilirubin=request.form['Total_Bilirubin']
    Direct_Bilirubin=request.form['Direct_Bilirubin']
    Alkaline_Phosphotase=request.form['Alkaline_Phosphotase']
    Alamine_Aminotransferase=request.form['Alamine_Aminotransferase']
    Aspartate_Aminotransferase=request.form['Aspartate_Aminotransferase']
    Total_Protiens=request.form['Total_Protiens']
    Albumin=request.form['Albumin']
    Albumin_and_Globulin_Ratio=request.form['Albumin_and_Globulin_Ratio']
    data=[[float(Age),float(Gender),float(Total_Bilirubin),float(Direct_Bilirubin),float(Alkaline_Phosphotase),float(Alamine_Aminotransferase),float(Aspartate_Aminotransferase),float(Total_Protiens),float(Albumin),float(Albumin_and_Globulin_Ratio)]]
    print(data)
    model = pickle.load(open('ETCC.pkl', 'rb'))
    prediction=model.predict(data)
    print(prediction)
    if prediction[0]==0:
        prediction='You dont have a liver disease'
    else:
        prediction='You have a liver disease problem,You must and should consult a doctor.Take care.'
    return render_template('predict.html',output=prediction)
if __name__=='__main__':
        app.run()

