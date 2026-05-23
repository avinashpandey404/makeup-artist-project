from flask import Blueprint, request, jsonify

from services.contact_service import create_contact

contact_bp = Blueprint('contact_bp', __name__)

@contact_bp.route('/api/contact', methods=['POST'])
def contact():

    data = request.get_json()

    required_fields = ['name', 'email', 'message']

    for field in required_fields:

        if field not in data or data[field] == '':
            return jsonify({
                "error": f"{field} is required"
            }), 400

    result = create_contact(data)

    return jsonify(result), 201
