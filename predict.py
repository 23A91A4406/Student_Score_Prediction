import pandas as pd
import joblib


model = joblib.load("models/model.pkl")


hours = float(input("Hours Studied : "))

attendance = float(input("Attendance : "))

sleep = float(input("Sleep Hours : "))

assignments = float(input("Assignments Completed : "))



input_data = pd.DataFrame({

'Hours_Studied':[hours],

'Attendance':[attendance],

'Sleep_Hours':[sleep],

'Assignments_Completed':[assignments]

})



prediction = model.predict(input_data)



predicted_score = max(0,min(100,prediction[0]))



print("\nPredicted Score")

print(round(predicted_score,2))
