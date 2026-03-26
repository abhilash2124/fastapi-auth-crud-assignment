# 🚀 FastAPI + React Full Stack Assignment

## 📌 Project Overview

This project is a scalable full-stack application built using **FastAPI (Backend)** and **React (Frontend)**. It implements secure authentication, role-based access control, and full CRUD operations for task management.

---

## 🔥 Features

### 🔐 Authentication

* User Registration
* User Login
* Password Hashing (bcrypt)
* JWT-based Authentication

### 👥 Role-Based Access

* User → Manage own tasks
* Admin → Can delete any task

### 📦 Task Management (CRUD)

* Create Tasks
* Read Tasks
* Update Tasks
* Delete Tasks

### 🌐 Frontend (React)

* Login & Register UI
* Dashboard for tasks
* API integration using Axios
* Displays success/error messages

### ⚙️ Backend Features

* REST API with FastAPI
* API Versioning (`/api/v1`)
* SQLAlchemy ORM
* Input validation with Pydantic
* Swagger API Docs (`/docs`)

---

## 🛠️ Tech Stack

### Backend

* FastAPI
* SQLAlchemy
* SQLite (can be upgraded to PostgreSQL)
* JWT (python-jose)
* Passlib (bcrypt)

### Frontend

* React.js
* Axios

---

## 📂 Project Structure

backend-api/
├── app/
│ ├── core/
│ ├── models/
│ ├── routes/
│ ├── schemas/
│ ├── database.py
│ └── main.py
├── frontend/
│ ├── src/
│ │ ├── pages/
│ │ ├── services/
│ │ └── App.js
├── requirements.txt
└── README.md

---

## 🚀 How to Run the Project

### 🔹 Backend

```bash
cd backend-api
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

👉 Runs at: http://127.0.0.1:8000
👉 API Docs: http://127.0.0.1:8000/docs

---

### 🔹 Frontend

```bash
cd frontend
npm install
npm start
```

👉 Runs at: http://localhost:3000

---

## 🔑 API Endpoints (v1)

### Auth

* POST `/api/v1/auth/register`
* POST `/api/v1/auth/login`

### Tasks

* GET `/api/v1/tasks`
* POST `/api/v1/tasks`
* PUT `/api/v1/tasks/{id}`
* DELETE `/api/v1/tasks/{id}`

---

## 🔒 Security Features

* JWT token authentication
* Password hashing using bcrypt
* Protected routes using token verification
* Role-based authorization

---

## 📈 Scalability Approach

This system is designed to scale with the following improvements:

* Replace SQLite with PostgreSQL for production
* Add Redis caching for faster performance
* Use Docker for containerized deployment
* Implement load balancing for high traffic
* Extend into microservices architecture

---

## 📌 Future Improvements

* Add UI enhancements (styling)
* Implement refresh tokens
* Add pagination for tasks
* Deploy on cloud (Render / AWS)

---

## 👨‍💻 Author

**Abhilash Addagatla**

---

## 📬 Submission

This project was developed as part of a Backend Developer Internship Assignment.

---
