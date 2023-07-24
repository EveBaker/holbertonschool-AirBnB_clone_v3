#!/usr/bin/python3
"""init BP views"""
import json
from api.v1.views import states_bp
from api.v1.views.states import *


def load_states():
    with open('states.json', 'r') as f:
        data = json.load(f)

    for state in data:
        state.create(name=state['name'])


def init_app(app):
    app.register_blueprint(states_bp)
    
    load_states()
