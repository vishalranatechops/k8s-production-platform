# K8s Production Platform

A production-style DevOps project demonstrating containerized application deployment, Kubernetes orchestration, CI/CD, monitoring, observability, scaling, and troubleshooting.

## Technology Stack

* Git / GitHub
* Docker
* Kubernetes
* Python
* GitHub Actions
* Prometheus
* Grafana

## Architecture

The project will implement the following workflow:

```text
GitHub
   ↓
CI/CD
   ↓
Docker Image
   ↓
Kubernetes
   ↓
Application
   ↓
Prometheus
   ↓
Grafana
```

## Project Components

### Application

A simple Python application that will expose health and application endpoints.

### Docker

The application will be packaged as a Docker container.

### Kubernetes

The application will be deployed using Kubernetes Deployment, Service, Ingress, ConfigMap, Secret, probes, resource limits, and HPA.

### Monitoring

Prometheus and Grafana will be used for application and Kubernetes monitoring.

### CI/CD

GitHub Actions will be used to automate application validation and Docker image creation.

## Project Status

**Day 1 — Project Foundation**

Project structure and Git repository setup.

## Future Work

* Build application
* Create Docker image
* Deploy application to Kubernetes
* Configure Service and Ingress
* Configure health probes
* Implement HPA
* Install Prometheus
* Configure Grafana
* Create dashboards
* Configure alerts
* Implement CI/CD
* Perform Kubernetes troubleshooting scenarios

