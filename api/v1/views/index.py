#!/usr/bin/python3
"""index.py to connect to API"""
from api.v1.views import app_views
from flask import Flask, Blueprint, jsonify
from models import storage


@app_views.route('/status', strict_slashes=False)
def hbnbStatus():
    """hbnbStatus"""
    return jsonify({"status": "OK"})


bp = Blueprint('stats', __name__)


@bp.route('/stats', strict_slashes=False)
def stats():
    """retrieves the number of each kind of obj by type"""
    stats = {}
    for cls in storage.classes():
        stats[cls.__name__] = storage.count(cls)
    return jsonify(stats)

app_views.register_blueprint(bp)
