#!/usr/bin/python3
"""Create a new view for Places objects
that handles all default RESTFul API actions:"""
from flask import Blueprint, request, jsonify
from app.models import Place, City, User


places_bp = Blueprint('places', __name__)


@places_bp.route('/api/v1/cities/<int:city_id>/places',
                 methods=['GET'])
def get_places(city_id):
    city = City.query.get(city_id)
    if not city:
        return jsonify({'message': 'City not found'}), 404

    places = city.places
    return jsonify([place.to_dict() for place in places]), 200


@places_bp.route('/api/v1/places/<int:place_id>',
                 methods=['GET'])
def get_place(place_id):
    place = Place.query.get(place_id)
    if not place:
        return jsonify({'message': 'Place not found'}), 404

    return jsonify(place.to_dict()), 200


@places_bp.route('/api/v1/places',
                 methods=['POST'])
def create_place():
    data = request.get_json()
    if not data:
        return jsonify({'message': 'Not a JSON'}), 400

    if 'user_id' not in data:
        return jsonify({'message': 'Missing user_id'}), 400

    user = User.query.get(data['user_id'])
    if not user:
        return jsonify({'message': 'User not found'}), 404

    if 'name' not in data:
        return jsonify({'message': 'Missing name'}), 400

    place = Place(
        name=data['name'],
        user_id=data['user_id'],
        city_id=data['city_id']
    )
    place.save()

    return jsonify(place.to_dict()), 201


@places_bp.route('/api/v1/places/<int:place_id>',
                 methods=['PUT'])
def update_place(place_id):
    data = request.get_json()
    if not data:
        return jsonify({'message': 'Not a JSON'}), 400

    place = Place.query.get(place_id)
    if not place:
        return jsonify({'message': 'Place not found'}), 404

    for key, value in data.items():
        if key in ['id', 'user_id', 'city_id', 'created_at', 'updated_at']:
            continue

        setattr(place, key, value)

    place.save()

    return jsonify(place.to_dict()), 200


@places_bp.route('/api/v1/places/<int:place_id>',
                 methods=['DELETE'])
def delete_place(place_id):
    place = Place.query.get(place_id)
    if not place:
        return jsonify({'message': 'Place not found'}), 404

    place.delete()

    return jsonify({'message': 'Place deleted'}), 200
