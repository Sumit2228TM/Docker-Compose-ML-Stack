# Docker ML Backend Stack

A real-world, production-style **Docker Compose ML backend** using:

- FastAPI (API service)
- PostgreSQL (persistent database)
- Jupyter Notebook (experimentation & analysis) 

Built **locally first** to understand multi-container orchestration before cloud deployment.

---

## 🚀 Tech Stack

- **FastAPI** – REST API for predictions
- **PostgreSQL 15** – Persistent relational database
- **Jupyter (SciPy Notebook)** – ML experimentation
- **Docker & Docker Compose** – Service orchestration

---

## 🧠 Architecture Overview

Client → FastAPI → PostgreSQL
↑
Jupyter Notebook

yaml
Copy code

- Services communicate over an internal Docker network
- PostgreSQL uses a named volume for persistence
- Database initializes automatically using `init.sql`

---

## 📁 Project Structure

```
docker-ml-backend-stack/
├── api/ # FastAPI service
├── notebooks/ # Jupyter notebooks
├── init.sql # DB initialization
├── docker-compose.yml # System orchestration
```

---

## ✅ Prerequisites

- Docker Desktop (running)
- Docker Compose

Verify:

```
docker --version
docker-compose --version
```
---

## ▶️ Run the Entire Stack

From the project root:

```
docker-compose up -d
```

First run may take a few minutes.

Check status:

```
docker-compose ps
```

Expected:

```
ml-postgres   Up
ml-api        Up
ml-jupyter    Up
```

## 🌐 Access Services
FastAPI Docs

http://localhost:8000/docs
Available endpoints:

POST /predict

GET /history

Jupyter Notebook
```
http://localhost:8888
```

Work directory: /work

## 🐞 Logs & Debugging
```
docker-compose logs api
docker-compose logs postgres
docker-compose logs -f api
```

## ⛔ Stop Services Safely
```
docker-compose stop
```

Remove containers (keep data):

```
docker-compose down
```
⚠️ Full wipe (removes DB data):

```
docker-compose down -v
```

## ❌ Common Mistakes
Running Docker Compose inside /api

Using localhost instead of postgres as DB host

Forgetting init.sql

Using down -v unintentionally

## 🎯 Why This Repo Matters
This project demonstrates industry-grade backend patterns:

Multi-container systems

Service discovery

Health checks

Persistent storage

ML-ready architecture

Perfect foundation before deploying to AWS, GCP, or Kubernetes.# Docker-Compose-ML-Stack

A production-style Docker Compose stack for an ML backend featuring FastAPI, PostgreSQL, and Jupyter Notebook. Demonstrates multi-container orchestration, service discovery, persistent volumes, and database-backed APIs — built and tested locally.
