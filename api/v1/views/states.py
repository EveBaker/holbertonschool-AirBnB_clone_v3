#!/usr/bin/python3
"""Create a new view for State objects that handles
all default RESTFul API actions"""
from flask import Blueprint, jsonify, request, abort
from models import State



@bp.route('/states', methods=['GET'])
def get_states():
    """Retrieves all State objects."""
    states = State.query.all()
    return jsonify([state.to_dict() for state in states])

@bp.route('/states/<id>', methods=['GET'])
def get_state(id):
    """Retrieves a State object by ID."""
    state = State.query.get(id)
    if state is None:
        abort(404, description='State not found')
    return jsonify(state.to_dict())

@bp.route('/states', methods=['POST'])
def create_state():
    """Creates a new State object."""
    data = request.get_json()

    if not data:
        abort(400, description='Not a JSON')

    if 'name' not in data:
        abort(400, description='Missing name')

    state = State(name=data['name'])
    state.save()
    return jsonify(state.to_dict()), 201

@bp.route('/states/<id>', methods=['PUT'])
def update_state(id):
    """Updates a State object by ID."""
    data = request.get_json()

    if not data:
        abort(400, description='Not a JSON')

    state = State.query.get(id)
    if state is None:
        abort(404, description='State not found')

    for key, value in data.items():
        if key in ('id', 'created_at', 'updated_at'):
            continue
        state.__setattr__(key, value)

    state.save()
    return jsonify(state.to_dict()), 200

@bp.route('/states/<id>', methods=['DELETE'])
def delete_state(id):
    """Deletes a State object by ID."""
    state = State.query.get(id)
    if state is None:
        abort(404, description='State not found')
    state.delete()
    return jsonify({}), 200
