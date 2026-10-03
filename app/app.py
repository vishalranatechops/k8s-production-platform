from flask import Flask, jsonify
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUEST_COUNT = Counter(
    "order_api_requests_total",
    "Total number of requests received by the Order API"
)


@app.before_request
def count_request():
    REQUEST_COUNT.inc()


@app.route("/")
def home():
    return jsonify({
        "application": "Order Management API",
        "version": "1.0",
        "status": "running"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/api/orders")
def orders():
    return jsonify({
        "orders": [
            {
                "id": 1001,
                "customer": "Customer-A",
                "status": "completed"
            },
            {
                "id": 1002,
                "customer": "Customer-B",
                "status": "processing"
            }
        ]
    })


@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {
        "Content-Type": CONTENT_TYPE_LATEST
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
