#!/usr/bin/python3
"""Initialize Blueprint views"""
import json


def load_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)


def init():
    data = load_json('states.json')
    for state in data:
        state(name=state['name']).save()


if __name__ == '__main__':
    init()
