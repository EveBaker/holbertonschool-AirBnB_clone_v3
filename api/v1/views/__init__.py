#!/usr/bin/python3
"""Initialize Blueprint views"""
import json
from api.v1.views import states_bp


def load_states():
    with open('states.json', 'r') as f:
        data = json.load(f)

    for state in data:
        State.create(name=state['name'])


def init_app(app):
    app.register_blueprint(states_bp)

    load_states()
