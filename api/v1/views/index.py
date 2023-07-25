#!/usr/bin/python3
"""index.py to connect to API """
from api.v1.views import app_views
from flask import jsonify


hbnbText = {
    "amenities": "Amenity",
    "cities": "City",
    "places": "Place",
    "reviews": "Review",
    "states": "State",
    "users": "User"
}


@app_views.route('/status', strict_slashes=False)
def hbnbStatus():
    """hbnbStatus"""
    return jsonify({"status": "OK"})


@app_views.route('/stats')
def stats():
    """returns API stats"""
    from models import storage
    classes = {
        "Amenity": "amenities",
        "City": "cities",
        "Place": "places",
        "Review": "reviews",
        "State": "states",
        "User": "users"
    }
    return jsonify({k: storage.count(v) for k, v in classes.items()})