# from flask import Blueprint, request, jsonify
# from extensions import db
# # from models import Snippet
# from schemas import SnippetSchema
#
# snippets_bp = Blueprint('snippets_bp', __name__)
# schema = SnippetSchema()
#
# @snippets_bp.route('/', methods=['POST'])
# def save_snippet():
#     data = request.get_json()
#     snippet = Snippet(source=data['source'], lang_id=data['lang_id'])
#     db.session.add(snippet); db.session.commit()
#     return schema.jsonify(snippet), 201
#
# @snippets_bp.route('/<int:id>', methods=['GET'])
# def get_snippet(id):
#     snippet = Snippet.query.get_or_404(id)
#     return schema.jsonify(snippet)
