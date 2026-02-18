"""
WSGI entry point for PythonAnywhere deployment.
Wraps FastAPI ASGI app for WSGI compatibility.
"""
from a2wsgi import ASGIMiddleware
from app.main import app

# Wrap FastAPI ASGI app for WSGI servers
application = ASGIMiddleware(app)
