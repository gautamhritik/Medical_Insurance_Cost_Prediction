# 🏥 Medical Insurance Cost Prediction & Risk Classification

A Machine Learning web application that predicts **medical insurance cost** and classifies **risk level** based on user inputs such as age, BMI, smoking habits, and more.

Deployed using **Streamlit Cloud**.

---

## 🚀 Live Demo

👉 https://medical-insurance-cost-prediction-ahg.streamlit.app

---

## 📌 Features

* 💰 Predicts **Insurance Cost**
* ⚠️ Classifies **Risk Level (Low / Medium / High)**
* 📊 Real-time user input via interactive UI
* 🧠 Built using Machine Learning models:

  * Regression Model → Cost Prediction
  * Classification Model → Risk Level

---

## 🧠 Tech Stack

* **Frontend/UI**: Streamlit
* **Backend**: Python
* **ML Models**: Scikit-learn
* **Data Processing**: Pandas, NumPy
* **Model Serialization**: Pickle

---

## 📂 Project Structure

```
Medical_Insurance_Cost_Prediction/
│
├── app.py                # Streamlit application
├── rf_model.pkl          # Regression model
├── rfc_model.pkl         # Classification model
├── features.pkl          # Feature columns used in training
├── scaler.pkl            # (Optional) Feature scaler
├── insurance.csv         # Dataset
├── code.ipynb            # Model training notebook
├── requirements.txt      # Dependencies
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```
git clone https://github.com/gautamhritik/Medical_Insurance_Cost_Prediction.git
cd Medical_Insurance_Cost_Prediction
```

### 2. Create a virtual environment

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Run the app

```
streamlit run app.py
```

---

## 📊 Input Features

* Age
* Sex
* BMI
* Number of Children
* Smoker Status
* Region

Additional engineered features:

* BMI Category
* Smoker × BMI Interaction

---

## 📈 Model Details

* **Regression Model (Random Forest)**
  Predicts insurance charges

* **Classification Model (Random Forest Classifier)**
  Predicts risk level

---

## ⚠️ Important Notes

* Ensure **same dependency versions** are used while training and deployment
* Pickle files are version-sensitive
* `features.pkl` must match training columns exactly

---

## 🧠 Future Improvements

* Use **joblib** or **ONNX** for better model portability
* Add **model evaluation metrics UI**
* Deploy using **Docker for environment consistency**
* Improve UI/UX design

---

## 👨‍💻 Author

**Hritik Gautam**

---

## 📜 License

This project is for educational purposes.
