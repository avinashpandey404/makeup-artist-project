from flask import Blueprint, request, jsonify

from services.booking_service import create_booking

booking_bp = Blueprint('booking_bp', __name__)

@booking_bp.route('/api/book', methods=['POST'])
def book_appointment():

    data = request.get_json()

    required_fields = ['name', 'email', 'phone', 'date', 'service']

    for field in required_fields:

        if field not in data or data[field] == '':
            return jsonify({
                "error": f"{field} is required"
            }), 400

    result = create_booking(data)

    return jsonify(result), 201
