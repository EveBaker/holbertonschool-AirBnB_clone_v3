#!/usr/bin/python3
"""app.py to connect to API
"""
import os
import sys
from api.v1.views import app_views
from flask import Flask
from models import storage


app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown_db(code):
    """Close storage on teardown."""
    storage.close()

if __name__ == "__main__":
    app.run(host=os.getenv('HBNB_API_HOST', '0.0.0.0'),
            port=int(os.getenv('HBNB_API_PORT', '5000')))