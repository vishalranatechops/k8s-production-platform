# Day 4 – Kubernetes Deployment and Service

## 1. Objective

In Day 4, we deployed the `order-api` application on Kubernetes and exposed it internally using a Kubernetes Service.

The implementation includes:

* Kubernetes Namespace
* Deployment
* Multiple Pods
* Kubernetes Service
* Service-to-Pod communication
* Endpoint verification

---

## 2. Kubernetes Resources

The application is deployed in the `order-api` namespace.

```text
Namespace
   │
   └── Deployment
          │
          ├── Pod 1
          │
          └── Pod 2
                 │
                 ▼
             Service
```

---

## 3. Namespace

The Namespace provides an isolated logical environment for the application.

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: order-api
```

Check the namespace:

```bash
kubectl get namespace
```

---

## 4. Deployment

The Deployment manages the application Pods.

It provides:

* Desired number of replicas
* Pod creation
* Pod replacement
* Self-healing
* Rolling update capability

Example:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: order-api
  namespace: order-api
spec:
  replicas: 2
  selector:
    matchLabels:
      app: order-api
  template:
    metadata:
      labels:
        app: order-api
    spec:
      containers:
        - name: order-api
          image: <application-image>
          ports:
            - containerPort: 8080
```

Verify:

```bash
kubectl get deployment -n order-api
kubectl get pods -n order-api
```

Expected result:

```text
2 Pods running
```

---

## 5. Service
[O
A Kubernetes Service provides a stable network endpoint for accessing the Pods.

The Pods can be recreated and their IP addresses can change, but the Service provides a stable endpoint.

Example:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: order-api-service
  namespace: order-api
spec:
  selector:
    app: order-api
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8080
  type: ClusterIP
```

Apply the Service:

```bash
kubectl apply -f service.yaml
```

Verify:

[I```bash
kubectl get svc -n order-api
```

---

## 6. Service Selector

The Service uses:

```yaml
selector:
  app: order-api
```

The Deployment creates Pods with:

```yaml
labels:
  app: order-api
```

Because the labels match, the Service automatically discovers the Pods.

```text
Service Selector
       │
       ▼
app: order-api
       │
       ├── Pod 1
       │
       └── Pod 2
```

---

## 7. Endpoints

Endpoints show the actual Pod IP addresses receiving traffic from the Service.
[O
Check them using:

```bash
kubectl get endpoints order-api-service -n order-api
```

Because the Deployment has **2 Pods**, the Service has **2 matching endpoints**.

Example:

```text
NAME                ENDPOINTS
order-api-service   10.42.0.10:8080,10.42.0.11:8080
```

This confirms that the Service selector is correctly matching both Pods.

---

## 8. Port Mapping

The Service configuration contains:

```yaml
port: 80
targetPort: 8080
```

Meaning:

```text
Client
  │
  │ Port 80
  ▼
Service
[I  │
  │ targetPort 8080
  ▼
Pod
  │
  ▼
order-api application
```

* `port` = Port exposed by the Service
* `targetPort` = Port where the application is listening inside the Pod

---

## 9. Useful Commands

Check all resources:

```bash
kubectl get all -n order-api
```

Check Pods:

```bash
kubectl get pods -n order-api -o wide
```

Check Pod labels:

```bash
kubectl get pods -n order-api --show-labels
```

Check Deployment:

```bash
kubectl get deployment -n order-api
```

Check Service:

```bash
kubectl get svc -n order-api
```

Check endpoints:

```bash
kubectl get endpoints order-api-service -n order-api
```

Describe the Service:

```bash
kubectl describe svc order-api-service -n order-api
```

---

## 10. Real-World Example

Consider `order-api` running with two Pods:

```text
                    order-api-service
                    ClusterIP :80
                         │
                  ┌──────┴──────┐
                  │             │
                  ▼             ▼
              Pod 1          Pod 2
              :8080          :8080
```

If Pod 1 fails, Kubernetes can recreate the Pod through the Deployment.

The Service continues to provide a stable endpoint and routes traffic to available Pods.

This provides basic **high availability and load distribution**.

---

## 11. Key Interview Points

### What is a Deployment?

A Deployment manages replicated Pods and provides declarative updates, scaling, and rollout management.

### What is a Service?

A Service provides a stable network endpoint for accessing a set of Pods.

### Why do we need a Service?

Pod IPs are temporary and can change. A Service provides a stable virtual IP/DNS name.

### How does a Service find Pods?

Through label selectors.

### Why are there two endpoints?

Because two Pods match the Service selector.

### What happens if one Pod is deleted?

The Deployment creates a replacement Pod, and the Service updates its endpoints automatically.

---

## 12. Day 4 Validation

The following checks were performed:

```bash
kubectl get pods -n order-api
kubectl get deployment -n order-api
kubectl get svc -n order-api
kubectl get endpoints order-api-service -n order-api
```

Result:

* Deployment is running.
* Two application Pods are running.
* Service is created.
* Service selector matches the application Pods.
* Two endpoints are registered with the Service.

---

## 13. Files

The Kubernetes manifests are stored in:

```text
k8s/
├── namespace.yaml
├── deployment.yaml
└── service.yaml
```

Documentation:

```text
docs/
└── day-04-kubernetes-basics.md
```

