#!/usr/bin/python3
"""Create a new view for State objects that handles
all default RESTFul API actions:"""
from flask import jsonify, request, abort
from models import storage
from models.state import State
from api.v1.views import app_views


@app_views.route('/states',
                 methods=['GET'], strict_slashes=False)
def get_states():
    """list all infor for all states"""
    states = storage.all(State).values()
    states_json = [state.to_dict() for state in states]
    return jsonify(states_json)


@app_views.route('/states/<string:state_id>',
                 methods=['GET'], strict_slashes=False)
def get_state(state_id):
    """get state information for specified state"""
    state = storage.get("State", state_id)
    if state is not None:
        return jsonify(state.to_dict())
    abort(404)


@app_views.route('/states/<string:state_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_state(state_id):
    """deletes a state by state_id"""
    state = storage.get("State", state_id)
    if state is not None:
        state.delete(state)
        storage.save()
        return jsonify({})
    abort(404)


@app_views.route('/states/',
                 methods=['POST'], strict_slashes=False)
def post_state():
    """create a new state"""
    if not request.get_json():
        abort(400, 'Not a JSON')
    if 'name' not in request.get_json():
        abort(400, 'Missing name')
    state = State(**request.get_json())
    state.save()
    return jsonify(state.to_dict()), 201


@app_views.route('/states/<string:state_id>',
                 methods=['PUT'], strict_slashes=False)
def put_state(state_id):
    """update a state"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    if not request.get_json():
        abort(400, 'Not a JSON')
    for key, value in request.get_json().items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(state, key, value)
    state.save()
    return jsonify(state.to_dict())
