# Day 2 — Build the Application

## 1. Objective

Build a simple Order Management API that will later be containerized using Docker and deployed to Kubernetes.

## 2. Application

The application is built using Python and Flask.

It provides:

* Application information
* Health check
* Order API
* Prometheus metrics endpoint

## 3. Application Endpoints

| Endpoint      | Purpose                 |
| ------------- | ----------------------- |
| `/`           | Application information |
| `/health`     | Health check            |
| `/api/orders` | Sample order data       |
| `/metrics`    | Prometheus metrics      |

## 4. Why `/health`?

The `/health` endpoint will later be used by Kubernetes for:

* Liveness Probe
* Readiness Probe

This allows Kubernetes to determine whether the application is healthy and ready to receive traffic.

## 5. Why `/metrics`?

The `/metrics` endpoint exposes application metrics in Prometheus format.

Later in the project:

```text
Application
     ↓
/metrics
     ↓
Prometheus
     ↓
Grafana
```

## 6. Local Testing

The application was started locally using:

```bash
python app.py
```

The following endpoints were tested:

```bash
curl http://localhost:8080/
curl http://localhost:8080/health
curl http://localhost:8080/api/orders
curl http://localhost:8080/metrics
```

## 7. Day 2 Learning

Today I learned how the application will fit into the overall DevOps project.

The application will later be:

```text
Python Application
       ↓
Docker Image
       ↓
Kubernetes Pod
       ↓
Kubernetes Service
       ↓
Ingress
       ↓
Prometheus
       ↓
Grafana
```

## 8. Day 2 Completed

* [ ] Flask application created
* [ ] requirements.txt created
* [ ] Health endpoint tested
* [ ] Order API tested
* [ ] Metrics endpoint tested
* [ ] Application documentation created
* [ ] Changes committed to Git
