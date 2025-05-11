from flask import Blueprint, jsonify, request
from extensions import db
from models import Card


cards_bp = Blueprint('cards', __name__)

@cards_bp.route('/cards', methods=['GET'])
def get_cards():
    cards = Card.query.all()
    return jsonify([card.to_dict() for card in cards])


@cards_bp.route('/cards', methods=['POST'])
def create_card():
    data = request.get_json()

    card = Card(
        title=data['title'],
        subtitle=data['subtitle'],
        image=data['image'],
        icon=data['icon'],
        text=data['text'],
        description=data['description']
    )

    db.session.add(card)
    db.session.commit()

    return jsonify(card.to_dict()), 201
