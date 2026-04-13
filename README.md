# 💰 Personal Finance Manager

A lightweight full-stack application for tracking personal expenses, built with **FastAPI** and **Streamlit**.

## 🚀 Overview
This project provides a clean interface to manage your daily spending. It categorizes expenses and ensures data integrity through a relational database.

## ✨ Key Features
- **Category Management**: Add and remove expense categories.
- **Relational Logic**: Uses SQL Foreign Keys and Cascade Deletes (deleting a category clears its associated expenses).
- **Expense Logging**: Track title, amount, and descriptions for every transaction.
- **Data Visualization**: Real-time table view of your financial history.
- **Modern Tech Stack**: Fully asynchronous backend with Pydantic data validation.

## 🛠️ Tech Stack
- **Backend**: Python 3.x, FastAPI, SQLAlchemy, SQLite
- **Frontend**: Streamlit, Requests
- **Validation**: Pydantic v2

## 📦 Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/affectedd/finance-manager.git
cd finance-manager
```
### 2. Create a Virtual Environment
```bash
python -m venv .venv
# Activate on Windows:
.venv\Scripts\activate
# Activate on Mac/Linux:
source .venv/bin/activate
```
### 3. Install Requirements
```bash
pip install -r requirements.txt
```
## 🖥️ Running the App
You need to run the Backend and the Frontend simultaneously.

### 1. Start the API (Terminal 1):
```bash
uvicorn backend.app.main:app --reload
```

### 2. Start the UI (Terminal 2):
```bash
streamlit run frontend.py
```
### 📂 Project Structure
- **backend/app/main.py**: Main API entry point and database initialization.
- **backend/app/models.py**: Database tables (SQLAlchemy).
- **backend/app/schemas.py**: Data validation (Pydantic).
- **frontend.py**: Streamlit-based user interface.