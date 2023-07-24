#!/usr/bin/env python3
""" Users view """
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models import storage
from models.user import User

@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    """ Retrieves the list of all User objects """
    all_users = storage.all(User).values()