Docker Assignment

Project Overview

This project demonstrates communication between a Node.js Express frontend and a Flask backend using Docker and Docker Compose.

The frontend provides a user form where users can enter their name and email. The submitted data is sent to the Flask backend, which processes the request and returns a JSON response.

---

Technologies Used

Frontend

- Node.js
- Express.js
- EJS
- Axios

Backend

- Python
- Flask

Containerization

- Docker
- Docker Compose

Version Control

- Git
- GitHub

---

Project Structure

Docker-Assignment/

├── Backend/

│   ├── app.py

│   ├── requirements.txt

│   ├── Dockerfile

│   └── .dockerignore

│

├── Frontend/

│   ├── app.js

│   ├── package.json

│   ├── package-lock.json

│   ├── Dockerfile

│   ├── views/

│   │   └── index.ejs

│   └── .dockerignore

│

├── docker-compose.yml

├── .gitignore

└── README.md

---

Features

- User registration form
- Frontend to backend communication
- REST API implementation
- Docker containerization
- Docker Compose networking
- GitHub integration

---

How to Run the Project

Clone Repository

git clone <repository-url>

cd Docker-Assignment

Run Using Docker Compose

docker compose up --build

Open Browser

http://localhost:3000

---

API Endpoint

Submit Form Data

Endpoint:

POST /submit

Sample Request:

{
"name": "Shakti Kumar Behera",
"email": "shakti@gmail.com"
}

Sample Response:

{
"name": "Shakti Kumar Behera",
"email": "shakti@gmail.com",
"message": "Data Received"
}

---

Docker Configuration

Backend Container

- Python 3.11
- Flask Application
- Port 5000

Frontend Container

- Node.js 18
- Express Application
- Port 3000

---

Learning Outcomes

- Understanding Docker fundamentals
- Creating Docker images
- Working with Docker Compose
- Building frontend-backend applications
- GitHub repository management

---

Author

Shakti Kumar Behera

Docker Assignment Submission
