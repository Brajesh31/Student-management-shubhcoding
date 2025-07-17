# 🎓 Student Management System API

A full-featured **Student Management System** built with **Django**, **MongoDB**, and **Docker**, designed for easy CRUD operations, attendance tracking, and REST API consumption.

> 📦 Fully containerized with Docker & Docker Compose for quick setup.

---

## 📌 Features

- 🔁 **CRUD** for students
- 🔍 Search student by roll number
- 🧮 Mark student attendance
- 🌐 REST API with Django REST Framework
- 💾 MongoDB integration via Djongo
- 🐳 Dockerized setup for both backend & DB

---

## 🛠 Tech Stack

| Layer         | Technology              |
|---------------|--------------------------|
| Backend       | Django 3.2               |
| API Framework | Django REST Framework    |
| Database      | MongoDB (via Djongo)     |
| Containerization | Docker, Docker Compose |
| Environment   | Python 3.10              |

---

## 🚀 Getting Started

### 🧰 Prerequisites
- Docker
- Docker Compose

### 🧪 Run the project

```bash
# Clone the repo
git clone https://github.com/your-username/student-management-shubhcoding.git
cd student-management-shubhcoding

# Build & run containers
docker-compose up --build
