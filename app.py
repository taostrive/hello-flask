from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hello_world():
    return jsonify({"message": "Hello World"})


@app.route("/health")
def health():
    try:
        # Perform any health checks here, like connectivity to a database.
        # ...
        message = "App is healthy"
        status = 200
    except Exception as e:
        message = f"App is unhealthy: {e}"
        status = 503

    return jsonify({"message": message}), status


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
