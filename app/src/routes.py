from flask import jsonify, render_template

def register_routes(app):

    @app.get("/health")
    def health():
        return jsonify(status="ok")

    @app.get("/api/hello")
    def api_hello():
        return jsonify(message="Hello from Flask API")

    @app.get("/")
    def ui_home():
        return render_template("index.html", title="DevOps Cloud K8s Flask")

