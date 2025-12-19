import sys
import os

# allow imports from app/src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from main import create_app

def test_health_endpoint():
    app = create_app()
    client = app.test_client()

    res = client.get("/health")
    assert res.status_code == 200
    assert res.get_json() == {"status": "ok"}

