# README.md

````md
# AI-Powered DevSecOps CI/CD Platform

A cloud-native DevSecOps platform built using FastAPI, Docker, Kubernetes, GitHub Actions, Prometheus, and modern security automation tools.

The platform demonstrates:
- CI/CD automation
- Security scanning
- Containerization
- Monitoring
- Kubernetes deployment
- Cloud-native infrastructure

---

# Project Overview

The AI-Powered DevSecOps CI/CD Platform automates software testing, security analysis, monitoring, and deployment using modern DevOps and DevSecOps tools.

This project simulates a real-world production-style DevSecOps workflow with automated CI/CD pipelines, containerized deployments, monitoring systems, and Kubernetes orchestration.

---

# Features

## Backend Development
- FastAPI REST APIs
- Swagger API Documentation
- Health Check Endpoints
- Structured JSON Logging
- Error Simulation Endpoint

## DevOps & CI/CD
- GitHub Actions CI/CD Pipeline
- Automated Testing with Pytest
- Docker Containerization
- Docker Compose Orchestration

## DevSecOps Security Automation
- Bandit Static Security Analysis
- Trivy Container Vulnerability Scanning
- Gitleaks Secret Detection

## Monitoring & Observability
- Prometheus Metrics Monitoring
- Metrics Endpoint Exposure
- Application Telemetry Collection

## Kubernetes Deployment
- Kubernetes Deployments
- Kubernetes Services
- Namespace Isolation
- Pod Scaling using Minikube

---

# Tech Stack

| Category | Technologies |
|---|---|
| Backend | FastAPI, Python |
| Containerization | Docker, Docker Compose |
| CI/CD | GitHub Actions |
| Testing | Pytest |
| Security | Bandit, Trivy, Gitleaks |
| Monitoring | Prometheus |
| Orchestration | Kubernetes, Minikube |
| Version Control | Git, GitHub |

---

# Project Architecture

```text
User
  ↓
FastAPI Application
  ↓
Docker Container
  ↓
GitHub Actions CI/CD
  ↓
Security Scanning
  ├── Bandit
  ├── Trivy
  └── Gitleaks
  ↓
Prometheus Monitoring
  ↓
Kubernetes Deployment
````

---

# Folder Structure

```text
Ai-Devsecops/
│
├── app/
│   ├── routes/
│   ├── logger.py
│   ├── main.py
│   └── requirements.txt
│
├── tests/
│   └── test_main.py
│
├── monitoring/
│   └── prometheus.yml
│
├── k8s/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── namespace.yaml
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── docker-compose.yml
├── Dockerfile
└── README.md
```

---

# Installation & Setup

## Clone Repository

```bash
git clone <repository-url>
cd Ai-Devsecops
```

---

# Create Virtual Environment

```bash
python -m venv venv
```

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

---

# Install Dependencies

```bash
pip install -r app/requirements.txt
```

---

# Run Application Locally

```bash
uvicorn app.main:app --reload
```

Open:

```text
http://localhost:8000/docs
```

---

# Docker Setup

## Build Docker Image

```bash
docker build -t ai-devsecops-app ./app
```

## Run Docker Container

```bash
docker run -d -p 8000:8000 --name ai-devsecops-container ai-devsecops-app
```

---

# Docker Compose

## Start Services

```bash
docker compose up -d
```

## Stop Services

```bash
docker compose down
```

---

# Running Tests

```bash
pytest
```

---

# Security Scanning

## Bandit

```bash
bandit -r app
```

## Trivy

```bash
trivy image ai-devsecops-app
```

## Gitleaks

```bash
gitleaks detect --source . -v
```

---

# Monitoring with Prometheus

Open:

```text
http://localhost:9090
```

Metrics Endpoint:

```text
http://localhost:8000/metrics
```

---

# Kubernetes Deployment

## Start Minikube

```bash
minikube start
```

## Configure Docker Environment for Minikube

### PowerShell

```powershell
& minikube -p minikube docker-env --shell powershell | Invoke-Expression
```

---

# Build Docker Image

```bash
docker build -t ai-devsecops-app:latest ./app
```

---

# Deploy Kubernetes Resources

```bash
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

---

# Verify Pods

```bash
kubectl get pods -n ai-devsecops
```

---

# Access Application

```bash
minikube service ai-devsecops-service -n ai-devsecops
```

---

# CI/CD Pipeline

The project uses GitHub Actions to automate:

* Dependency installation
* Automated testing
* Security scanning
* Docker image validation
* Secret detection

Pipeline stages:

```text
Code Push
   ↓
GitHub Actions
   ↓
Pytest
   ↓
Bandit Scan
   ↓
Trivy Scan
   ↓
Gitleaks Scan
   ↓
Build Success
```

---

# Future Enhancements

* AI-based log analysis
* Incident prediction system
* Grafana dashboards
* AWS EKS deployment
* Helm charts
* Horizontal Pod Autoscaling
* AI chatbot for DevOps monitoring

---

# Learning Outcomes

This project helped in understanding:

* DevOps workflows
* CI/CD automation
* Cloud-native deployment
* Kubernetes orchestration
* Monitoring systems
* Container security
* Infrastructure automation
* DevSecOps practices

---

# Conclusion

The AI-Powered DevSecOps CI/CD Platform demonstrates modern DevOps, security automation, monitoring, and Kubernetes deployment practices.

The project simulates a real-world cloud-native infrastructure workflow and provides practical exposure to production-grade DevOps tools and methodologies.

```
```
