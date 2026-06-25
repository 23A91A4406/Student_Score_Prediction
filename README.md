# 🎓 Student Score Prediction using Machine Learning

## 📌 Project Overview

This project predicts a student's expected exam score based on study-related factors using Machine Learning.

The system analyzes various inputs such as:

* 📚 Hours Studied
* 🏫 Attendance Percentage
* 😴 Sleep Hours
* 📝 Assignments Completed

and predicts the student's score through an interactive Flask web application.

---

## 🚀 Features

✅ Dataset Generation

✅ Exploratory Data Analysis (EDA)

✅ Correlation Analysis

✅ Linear Regression Model

✅ Train-Test Split

✅ Model Evaluation

✅ Model Persistence using Joblib

✅ Flask Web Application

✅ Interactive Prediction Interface

✅ Professional UI Design

---

## 🛠️ Tech Stack

| Category         | Technologies        |
| ---------------- | ------------------- |
| Language         | Python              |
| Data Analysis    | Pandas, NumPy       |
| Visualization    | Matplotlib, Seaborn |
| Machine Learning | Scikit-Learn        |
| Web Framework    | Flask               |
| Model Saving     | Joblib              |
| IDE              | VS Code             |
| Version Control  | Git & GitHub        |

---

## 📂 Project Structure

```text
Student_Score_Prediction/

│── data/
│   └── student_scores.csv

│── models/
│   └── model.pkl

│── notebooks/
│   └── student_score.ipynb

│── templates/
│   └── index.html

│── static/

│── app.py
│── train.py
│── predict.py
│── requirements.txt
│── README.md
│── .gitignore
```

---

## 📊 Model Evaluation

The model is evaluated using:

* R² Score
* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)

---

## 🌐 Running the Application

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Train Model

```bash
python train.py
```

### Start Flask Application

```bash
python app.py
```

Open Browser:

```text
http://127.0.0.1:5000
```

---

## 🎯 Sample Prediction

| Feature               | Value |
| --------------------- | ----- |
| Hours Studied         | 8     |
| Attendance            | 95    |
| Sleep Hours           | 7     |
| Assignments Completed | 8     |

Predicted Score: **~95–100**