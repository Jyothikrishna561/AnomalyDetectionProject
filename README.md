# 🚨 AI Anomaly Detection System

## 📌 Overview

This project detects suspicious transactions using machine learning (Isolation Forest).

Users can:

* Enter transaction details manually
* Upload CSV files for bulk analysis

---

## 🖥️ UI Preview

![App Screenshot](screenshot.png)

---

## 🚀 Features

* Manual anomaly detection
* CSV upload and analysis
* FastAPI backend
* Clean dark UI

---

## 🛠️ Tech Stack

* FastAPI
* HTML, CSS, JavaScript
* Scikit-learn
* Uvicorn

---

## ▶️ Run Project

### Backend

cd backend
python -m uvicorn main:app --reload

### Frontend

cd frontend
python -m http.server 5500

Open: http://127.0.0.1:5500

---

## 📊 API

* POST /predict
* POST /upload-csv


