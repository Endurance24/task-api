# 🚀 Task API

A simple RESTful CRUD API built with **FastAPI** for the **FlyRank Backend AI Engineering Internship**.

This project demonstrates the implementation of a Task Management API using Python and FastAPI, featuring Create, Read, Update, and Delete (CRUD) operations with in-memory storage.

---

## 📌 Features

- Create a new task
- Retrieve all tasks
- Retrieve a task by ID
- Update an existing task
- Delete a task
- Health check endpoint
- Interactive API documentation with Swagger UI
- Proper HTTP status codes and error handling

---

## 🛠️ Tech Stack

- **Python 3.14**
- **FastAPI**
- **Uvicorn**
- **Pydantic**

---

## 📂 Project Structure

```text
task-api/
│── main.py
│── requirements.txt
│── README.md
│── .gitignore
└── venv/
```

> **Note:** The `venv` folder is excluded from GitHub using `.gitignore`.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Endurance24/task-api.git
```

### 2. Navigate into the project

```bash
cd task-api
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

#### Windows (PowerShell)

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the API

```bash
uvicorn main:app --reload
```

The API will start at:

```
http://127.0.0.1:8000
```

---

## 📖 API Documentation

FastAPI automatically generates interactive documentation.

### Swagger UI

```
http://127.0.0.1:8000/docs
```

### ReDoc

```
http://127.0.0.1:8000/redoc
```

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | API information |
| GET | `/health` | Health check |
| GET | `/tasks` | Retrieve all tasks |
| GET | `/tasks/{task_id}` | Retrieve a task by ID |
| POST | `/tasks` | Create a new task |
| PUT | `/tasks/{task_id}` | Update a task |
| DELETE | `/tasks/{task_id}` | Delete a task |

---

## 📝 Sample Request

### Create a Task

**POST** `/tasks`

```json
{
  "title": "Complete FlyRank Assignment"
}
```

### Sample Response

```json
{
  "id": 4,
  "title": "Complete FlyRank Assignment",
  "done": false
}
```

---

## 📷 API Preview

After running the application, open:

```
http://127.0.0.1:8000/docs
```

Take a screenshot of the Swagger UI and replace the placeholder below.

```text
docs/swagger-ui.png
```

Example:

```markdown
![Swagger UI](docs/swagger-ui.png)
```

---

## 🚀 Future Improvements

- Persistent database integration (SQLite or PostgreSQL)
- User authentication with JWT
- Task filtering and search
- Pagination
- Docker support
- Automated testing with Pytest

---

## 👨‍💻 Author

**Endurance Alexander**

- GitHub: https://github.com/Endurance24

---

## 📄 License

This project was developed as part of the **FlyRank Backend AI Engineering Internship** technical assessment and is intended for educational and evaluation purposes.