# 🚨 AI Anomaly Detection System

## 📌 Project Description

This project is a web-based application that detects anomalous (suspicious) transactions using machine learning. It simulates how real-world systems identify unusual behavior in areas like banking and cybersecurity.

---

## 🎯 Objective

The goal of this project is to build an end-to-end system that:

* Accepts user input or bulk data
* Processes the data using a machine learning model
* Identifies whether a transaction is normal or anomalous

---

## 🚀 Features

* 🔹 Manual input-based anomaly detection
* 🔹 CSV file upload for bulk analysis
* 🔹 Real-time prediction using API
* 🔹 Clean and interactive user interface
* 🔹 Displays results in table format

---

## 🛠️ Tech Stack

* **Backend:** Python, FastAPI
* **Frontend:** HTML, CSS, JavaScript
* **Machine Learning:** Scikit-learn (Isolation Forest)
* **Server:** Uvicorn

---

## 🧠 How It Works

1. User enters transaction details or uploads a CSV file
2. Frontend sends data to backend via API
3. Backend processes data using trained ML model
4. Model predicts whether data is normal or anomaly
5. Results are displayed on the UI

---

## 📂 Project Structure

```
AnomalyDetectionProject/
│
├── backend/        # FastAPI backend
├── frontend/       # UI (HTML, CSS, JS)
├── model/          # Trained ML model
├── dataset/        # Sample dataset
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run the Project

### 🔹 Step 1: Clone Repository

```
git clone <your-repo-link>
cd AnomalyDetectionProject
```

### 🔹 Step 2: Install Dependencies

```
pip install -r requirements.txt
```

### 🔹 Step 3: Run Backend

```
cd backend
python -m uvicorn main:app --reload
```

### 🔹 Step 4: Run Frontend

```
cd frontend
python -m http.server 5500
```

### 🔹 Step 5: Open in Browser

```
http://127.0.0.1:5500
```

---

## 📊 Future Improvements

* Add real-world datasets
* Improve model accuracy
* Add graphs and analytics
* Deploy as a live web application

---


