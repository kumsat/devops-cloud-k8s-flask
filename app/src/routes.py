import os
from flask import jsonify

def register_routes(app):

    @app.get("/health")
    def health():
        return jsonify(status="ok")

    @app.get("/api/hello")
    def hello():
        color = os.getenv("APP_COLOR", "unknown")
        return jsonify(message=f"Hello from {color} (Flask API)")

