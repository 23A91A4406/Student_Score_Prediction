import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error


df = pd.read_csv("data/student_scores.csv")


X = df.drop("Score",axis=1)
y = df["Score"]


X_train,X_test,y_train,y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
)


model = LinearRegression()

model.fit(X_train,y_train)


y_pred = model.predict(X_test)



r2 = r2_score(y_test,y_pred)

mae = mean_absolute_error(y_test,y_pred)

mse = mean_squared_error(y_test,y_pred)



print("\nModel Evaluation")
print("---------------------------")

print("R2 Score :",r2)

print("MAE :",mae)

print("MSE :",mse)



joblib.dump(model,"models/model.pkl")

print("\nModel Saved Successfully")