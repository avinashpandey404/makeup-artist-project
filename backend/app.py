from flask import Flask
from flask_cors import CORS

from routes.booking_routes import booking_bp
from routes.contact_routes import contact_bp
from routes.health_routes import health_bp

app = Flask(__name__)

CORS(app)

# Register Routes
app.register_blueprint(booking_bp)
app.register_blueprint(contact_bp)
app.register_blueprint(health_bp)

@app.route('/')
def home():
    return {
        "message": "Glow Beauty Studio Backend Running"
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
