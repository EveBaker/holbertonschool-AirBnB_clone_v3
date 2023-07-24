#!/usr/bin/python3
"""Initialize Blueprint views"""
from flask import Flask
from .views import bp


def create_app():
    app = Flask(__name__)

    # Import and register the blueprint
    app.register_blueprint(bp)

    return app
