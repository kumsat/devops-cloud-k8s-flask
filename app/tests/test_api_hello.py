import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from main import create_app

def test_api_hello():
    app = create_app()
    client = app.test_client()

    res = client.get("/api/hello")
    assert res.status_code == 200
    assert res.get_json()["message"] == "Hello from Flask API"

