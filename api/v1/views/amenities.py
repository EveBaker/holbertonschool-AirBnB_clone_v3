#!/usr/bin/python3
"""Create a new view for amenities objects that handles
all default RESTFul API actions:"""
from flask import abort, jsonify, make_response, request
from models.amenity import Amenity
from models import storage


def get_amenities():
  """lists all amenity objs"""
  amenities = [amenity.to_dict() for amenity in storage.all(Amenity)]
  return jsonify(amenities)

def get_amenity(amenity_id):
  """gets an amenity obj"""
  amenity = storage.get(Amenity, amenity_id)
  if not amenity:
    abort(404)
  return jsonify(amenity.to_dict())

def delete_amenity(amenity_id):
  """deletes amenity obj"""
  amenity = storage.get(Amenity, amenity_id)
  if not amenity:
    abort(404)
  storage.delete(amenity)
  return make_response(jsonify({}), 200)

def create_amenity():
  """creates an amenity dict"""
  data = request.get_json()
  if not data:
    abort(400, 'Not a JSON')
  if 'name' not in data:
    abort(400, 'Missing name')
  name = data['name']
  amenity = Amenity(name=name)
  storage.save(amenity)
  return jsonify(amenity.to_dict()), 201

def update_amenity(amenity_id):
  """ppdates an amenity obj"""
  amenity = storage.get(Amenity, amenity_id)
  if not amenity:
    abort(404)
  data = request.get_json()
  if not data:
    abort(400, 'Not a JSON')
  for key, value in data.items():
    if key in ('id', 'created_at', 'updated_at'):
      continue
    setattr(amenity, key, value)
  storage.save(amenity)
  return jsonify(amenity.to_dict()), 200
