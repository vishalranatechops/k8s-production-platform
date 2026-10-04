# Day 3 — Docker Containerization

## 1. Objective

The objective of Day 3 was to containerize the Python Flask Order Management API using Docker.

The application was created on Day 2 and runs locally using Python. On Day 3, the application was packaged into a Docker image and executed as a Docker container.

### Application Flow

```text
Python Flask Application
        ↓
Dockerfile
        ↓
Docker Image
        ↓
Docker Container
        ↓
Application running on port 8080
```

---

## 2. Project Structure

```text
k8s-production-platform/
├── app/
│   ├── app.py
│   └── requirements.txt
├── docker/
│   └── Dockerfile
├── k8s/
├── monitoring/
├── docs/
│   └── Day-3-Docker.md
├── .dockerignore
└── README.md
```

---

## 3. What is Docker?

Docker is a containerization platform that packages an application together with its dependencies so that it can run consistently across different environments.

Instead of installing Python and all application dependencies directly on every server, we package them inside a container image.

---

## 4. Image vs Container

### Docker Image

A Docker image is a packaged, read-only template containing the application, runtime, dependencies, and required filesystem components.

Example:

```text
order-api:v1
```

### Docker Container

A container is a running instance of a Docker image.

Example:

```text
order-api-container
```

### Simple Difference

```text
Image     → Template
Container → Running instance
```

---

## 5. Dockerfile

The Dockerfile defines how the application image should be created.

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

EXPOSE 8080

CMD ["python", "app.py"]
```

---

## 6. Dockerfile Explanation

### FROM

```dockerfile
FROM python:3.12-slim
```

Uses Python 3.12 slim as the base image.

The slim image is smaller than the full Python image and is suitable for our application.

### WORKDIR

```dockerfile
WORKDIR /app
```

Sets `/app` as the working directory inside the container.

### COPY

```dockerfile
COPY app/requirements.txt .
```

Copies the application's dependency file into the container.

### RUN

```dockerfile
RUN pip install --no-cache-dir -r requirements.txt
```

Installs the Python dependencies during image creation.

### COPY Application

```dockerfile
COPY app/ .
```

Copies the application source code into the container.

### EXPOSE

```dockerfile
EXPOSE 8080
```

Documents that the application uses port 8080.

### CMD

```dockerfile
CMD ["python", "app.py"]
```

Defines the default command executed when the container starts.

---

## 7. RUN vs CMD

An important Docker concept:

```text
RUN → executed while building the image

CMD → executed when the container starts
```

Example:

```dockerfile
RUN pip install -r requirements.txt
```

happens during:

```bash
docker build
```

Whereas:

```dockerfile
CMD ["python", "app.py"]
```

happens during:

```bash
docker run
```

---

## 8. .dockerignore

The project contains a `.dockerignore` file:

```text
.git
.gitignore
__pycache__
*.pyc
venv
.env
.vscode
.idea
```

### Purpose

`.dockerignore` prevents unnecessary files from being sent as part of the Docker build context.

For example, the local Python virtual environment does not need to be copied into the Docker image because the Dockerfile creates its own environment and installs the required dependencies.

---

## 9. Building the Docker Image

The image was built using:

```bash
docker build -t order-api:v1 -f docker/Dockerfile .
```

### Command Breakdown

```text
docker build
```

Build a Docker image.

```text
-t order-api:v1
```

Assign the image name `order-api` and tag it as `v1`.

```text
-f docker/Dockerfile
```

Specify the Dockerfile location.

```text
.
```

Use the current project directory as the Docker build context.

### Result

```text
order-api:v1
```

---

## 10. Build Context

The final `.` in the build command is important.

```bash
docker build -t order-api:v1 -f docker/Dockerfile .
```

It means:

> Use the current directory as the Docker build context.

This allows Docker to access:

```text
app/app.py
app/requirements.txt
```

while using:

```text
docker/Dockerfile
```

as the build instructions.

### Important Interview Point

```text
-f → Which Dockerfile?

.  → Which build context?
```

---

## 11. Running the Container

The container was started using:

```bash
docker run -d --name order-api-container -p 8080:8080 order-api:v1
```

### Command Breakdown

```text
docker run
```

Creates and starts a container from an image.

```text
-d
```

Runs the container in detached/background mode.

```text
--name order-api-container
```

Assigns a name to the container.

```text
-p 8080:8080
```

Maps the host port to the container port.

```text
order-api:v1
```

Specifies the image to run.

---

## 12. Port Mapping

The application listens on port 8080 inside the container.

```text
Host
8080
  │
  │ Docker port mapping
  ▼
Container
8080
  │
  ▼
Flask Application
```

Command:

```bash
-p 8080:8080
```

means:

```text
Host Port : Container Port
```

Therefore the application can be accessed using:

```text
http://localhost:8080
```

---

## 13. Checking Running Containers

Command:

```bash
docker ps
```

This displays currently running containers.

Expected container:

```text
order-api-container
```

---

## 14. Testing the Application

The following endpoints were tested:

### Root endpoint

```bash
curl http://localhost:8080/
```

### Health endpoint

```bash
curl http://localhost:8080/health
```

### Orders API

```bash
curl http://localhost:8080/api/orders
```

### Prometheus metrics

```bash
curl http://localhost:8080/metrics
```

The `/metrics` endpoint will later be used by Prometheus during the observability phase of the project.

---

## 15. Container Logs

Container logs can be viewed using:

```bash
docker logs order-api-container
```

This is useful when troubleshooting an application running inside a container.

For example, if the application crashes or fails to start, container logs can help identify the problem.

---

## 16. Useful Docker Commands Learned

### List images

```bash
docker images
```

### List running containers

```bash
docker ps
```

### List all containers

```bash
docker ps -a
```

### View logs

```bash
docker logs order-api-container
```

### Stop container

```bash
docker stop order-api-container
```

### Remove container

```bash
docker rm order-api-container
```

### Remove image

```bash
docker rmi order-api:v1
```

---

## 17. Docker Troubleshooting Lesson

During Day 3, the first Docker build attempt failed because the Docker build context was incorrect.

The Dockerfile was located at:

```text
docker/Dockerfile
```

while the application was located at:

```text
app/
```

The correct command from the project root was:

```bash
docker build -t order-api:v1 -f docker/Dockerfile .
```

This demonstrated the difference between the Dockerfile location and the Docker build context.

---

## 18. Final Day 3 Architecture

```text
                GitHub
                   │
                   ▼
          Python Flask Application
                   │
                   ▼
              Dockerfile
                   │
                   ▼
             Docker Build
                   │
                   ▼
             order-api:v1
             Docker Image
                   │
                   ▼
          order-api-container
             Docker Container
                   │
                   ▼
             Port 8080
                   │
                   ▼
              Flask API
```

---

## 19. Day 3 Interview Questions

### Q1. What is Docker?

Docker is a containerization platform used to package applications and their dependencies into portable containers.

### Q2. What is the difference between an image and a container?

An image is a packaged template, while a container is a running instance of that image.

### Q3. What is a Dockerfile?

A Dockerfile contains instructions used to build a Docker image.

### Q4. What is the purpose of `FROM`?

`FROM` specifies the base image used to build the Docker image.

### Q5. Difference between `RUN` and `CMD`?

`RUN` executes during image build time, while `CMD` executes when a container starts.

### Q6. What does `-p 8080:8080` mean?

It maps port 8080 on the Docker host to port 8080 inside the container.

### Q7. What is Docker build context?

The build context is the set of files and directories available to Docker during an image build. In our command, `.` represents the current project directory.

### Q8. Why use `.dockerignore`?

It prevents unnecessary files from being included in the Docker build context.

---

## 20. Day 3 Completion Checklist

* [x] Docker Desktop installed
* [x] Docker Engine running
* [x] Dockerfile created
* [x] `.dockerignore` created
* [x] Docker image built
* [x] `order-api:v1` image created
* [x] Docker container created
* [x] Port mapping configured
* [x] Application tested inside container
* [x] Container logs checked
* [x] Docker troubleshooting performed

---

## 21. Day 3 Summary

Day 3 converted the Python Flask application from a locally running application into a containerized application.

The final flow is:

```text
Python Application
        ↓
Dockerfile
        ↓
Docker Image
        ↓
Docker Container
        ↓
Flask API
```

The containerized application is now ready for the next stage of the project: deploying it on Kubernetes.

