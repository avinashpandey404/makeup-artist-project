from flask import Blueprint

health_bp = Blueprint('health_bp', __name__)

@health_bp.route('/health', methods=['GET'])
def health():

    return {
        "status": "healthy"
    }, 200
