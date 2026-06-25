from flask import Flask,render_template,request
import pandas as pd
import joblib


app = Flask(__name__)


model = joblib.load("models/model.pkl")



@app.route('/')
def home():

    return render_template("index.html")




@app.route('/predict',methods=['POST'])

def predict():



    hours = float(request.form['hours'])

    attendance = float(request.form['attendance'])

    sleep = float(request.form['sleep'])

    assignments = float(request.form['assignments'])




    input_data = pd.DataFrame({

        'Hours_Studied':[hours],

        'Attendance':[attendance],

        'Sleep_Hours':[sleep],

        'Assignments_Completed':[assignments]

    })



    prediction = model.predict(input_data)



    predicted_score = round(max(0,min(100,prediction[0])),2)



    return render_template(
'index.html',
prediction=predicted_score
)




if __name__ == '__main__':

    app.run(debug=True)
