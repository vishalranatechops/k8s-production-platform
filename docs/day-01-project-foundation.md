# Day 1 — Project Foundation

## 1. Project Name

**K8s Production Platform**

## 2. Project Objective

The objective of this project is to build and deploy a containerized application on Kubernetes and implement monitoring and observability using Prometheus and Grafana.

The project will demonstrate a complete DevOps workflow from source code to containerization, Kubernetes deployment, monitoring, scaling, and troubleshooting.

## 3. Technologies

* Git / GitHub
* Docker
* Kubernetes
* Prometheus
* Grafana
* GitHub Actions
* Python application

## 4. High-Level Project Flow

```text
Developer
    ↓
Git / GitHub
    ↓
CI Pipeline
    ↓
Docker Image
    ↓
Container Registry
    ↓
Kubernetes
    ↓
Application
    ↓
Prometheus
    ↓
Grafana
```

## 5. Kubernetes Components Planned

The project will use:

* Namespace
* Deployment
* ReplicaSet
* Pods
* Service
* Ingress
* ConfigMap
* Secret
* Resource Requests/Limits
* Liveness Probe
* Readiness Probe
* HPA
* NetworkPolicy
* ServiceMonitor
* PrometheusRule

## 6. Monitoring

Prometheus will collect application and Kubernetes metrics.

Grafana will be used to visualize:

* CPU utilization
* Memory utilization
* Pod restarts
* Request rate
* Error rate
* Application health
* Number of replicas

## 7. Troubleshooting Scenarios

The project will include practical troubleshooting scenarios such as:

* Pod in CrashLoopBackOff
* OOMKilled Pod
* Service with no endpoints
* Failed deployment
* High CPU utilization
* High memory utilization
* HPA scaling
* Application health-check failure

## 8. Project Goal

The final project should demonstrate an end-to-end DevOps workflow and provide practical experience in deploying, monitoring, scaling, and troubleshooting a Kubernetes-based application.

## 9. Day 1 Completed

* [ ] Project directory created
* [ ] Git initialized
* [ ] Project structure created
* [ ] Initial README created
* [ ] Initial Git commit created
* [ ] GitHub repository created
* [ ] Project pushed to GitHub

