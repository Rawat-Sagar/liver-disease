from flask import Flask , render_template , request
import pickle
import numpy as np


app = Flask(__name__)

filename = 'liver_prediction_pickle'
model = pickle.load(open(filename,'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    Age = float(request.form['Age'])
    Gender  = float(request.form['Gender'])
    Total_Bilirubin = float(request.form['Total_Bilirubin'])
    Direct_Bilirubin = float(request.form['Direct_Bilirubin'])
    Alkaline_Phosphotase = float(request.form['Alkaline_Phosphotase'])
    Alamine_Aminotransferase = float(request.form['Alamine_Aminotransferase'])
    Aspartate_Aminotransferase = float(request.form['Aspartate_Aminotransferase'])
    Total_Protiens = float(request.form['Total_Protiens'])
    Albumin = float(request.form['Albumin'])
    Albumin_and_Globulin_Ratio = float(request.form['Albumin_and_Globulin_Ratio'])

    data = np.array([[Age,Gender,Total_Bilirubin,Direct_Bilirubin,Alkaline_Phosphotase,Alamine_Aminotransferase,Aspartate_Aminotransferase, Total_Protiens,Albumin,Albumin_and_Globulin_Ratio]])
    my_prediction = model.predict(data)

    return render_template('index.html',
    Age = str(Age),
    Gender = str(Gender),
    Total_Bilirubin = str(Total_Bilirubin),
    Direct_Bilirubin = str(Direct_Bilirubin),
    Alkaline_Phosphotase = str(Alkaline_Phosphotase),
    Alamine_Aminotransferase = str(Alamine_Aminotransferase),
    Aspartate_Aminotransferase = str(Aspartate_Aminotransferase),
    Total_Protiens = str(Total_Protiens),
    Albumin = str(Albumin),
    Albumin_and_Globulin_Ratio = str(Albumin_and_Globulin_Ratio),
    prediction=my_prediction)

if __name__ == '__main__':
    app.run(debug=True)