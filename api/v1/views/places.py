#!/usr/bin/python3
"""Create a new view for Place objectsthat
handles all default RESTFul API actions:"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models import storage
from models.city import City
from models.place import Place
from models.user import User


@app_views.route('/api/v1/cities/<int:city_id>/places', methods=['GET'])
def get_places(city_id):
    "list all places"
    city = City.query.get(city_id)
    if not city:
        abort(404)

    places = city.places
    return jsonify([place.to_dict() for place in places]), 200


@app_views.route('/api/v1/places/<int:place_id>', methods=['GET'])
def get_place(place_id):
    """get place by id"""
    place = Place.query.get(place_id)
    if not place:
        abort(404)

    return jsonify(place.to_dict()), 200


@app_views.route('/places/<string:place_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_place(place_id):
    """deletes a place by id"""
    place = storage.get("Place", place_id)
    if place is None:
        abort(404)
    place.delete()
    storage.save()
    return (jsonify({}))


@app_views.route('/api/v1/places', methods=['POST'])
def post_place():
    """make a place"""
    data = request.get_json()
    if not data:
        abort(400, message='Not a JSON')

    if 'user_id' not in data:
        abort(400, message='Missing user_id')

    user = User.query.get(data['user_id'])
    if not user:
        abort(404, message='User not found')

    if 'name' not in data:
        abort(400, message='Missing name')

    place = Place(
        name=data['name'],
        user_id=data['user_id'],
        city_id=data['city_id']
    )
    place.save()

    return jsonify(place.to_dict()), 201


@app_views.route('/api/v1/places/<int:place_id>', methods=['PUT'])
def put_place(place_id):
    """update a place by id"""
    data = request.get_json()
    if not data:
        abort(400, message='Not a JSON')

    place = Place.query.get(place_id)
    if not place:
        abort(404, message='Place not found')

    for key, value in data.items():
        if key in ['id', 'user_id', 'city_id', 'created_at', 'updated_at']:
            continue

        setattr(place, key, value)

    place.save()

    return jsonify(place.to_dict()), 200
