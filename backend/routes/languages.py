from flask import Blueprint, jsonify, current_app
import requests

languages_bp = Blueprint('languages_bp', __name__)

@languages_bp.route('/', methods=['GET'])
def list_languages():
    resp = requests.get(f"{current_app.config['JUDGE0_URL']}/languages")
    return jsonify(resp.json())
