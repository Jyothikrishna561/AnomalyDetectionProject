# 🚨 AI Anomaly Detection System

## 🔍 Overview

A web-based application that detects suspicious (anomalous) transactions using Machine Learning.

Users can:

* 🔹 Enter transaction details manually
* 🔹 Upload CSV files for bulk anomaly detection

---

## 🖥️ UI Preview

![App Screenshot](screenshot.png)

---

## ⚙️ Features

* ✅ Real-time anomaly detection
* ✅ CSV upload & batch processing
* ✅ FastAPI backend for high performance
* ✅ Clean dark-themed user interface

---

## 🛠️ Tech Stack

* **Backend:** FastAPI
* **Frontend:** HTML, CSS, JavaScript
* **ML Model:** Isolation Forest (Scikit-learn)
* **Server:** Uvicorn

---

## ▶️ How to Run

### 🔹 Backend

```bash
cd backend
python -m uvicorn main:app --reload
```

### 🔹 Frontend

```bash
cd frontend
python -m http.server 5500
```

👉 Open in browser:
http://127.0.0.1:5500

---

## 📡 API Endpoints

* `POST /predict` → Single transaction prediction
* `POST /upload-csv` → Bulk anomaly detection

---

## 📂 Project Structure

```
backend/    → FastAPI application
frontend/   → UI (HTML, CSS, JS)
dataset/    → Sample data
model/      → Trained ML model
```

---

## 🚀 Future Improvements

* 📊 Add analytics dashboard
* 🌍 Deploy online
* 🤖 Improve model accuracy



