from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

import os

from database.db import db
from services.booking_service import create_booking

# ==================================================
# LOAD ENV VARIABLES
# ==================================================

load_dotenv()

# ==================================================
# CREATE FLASK APP
# ==================================================

app = Flask(__name__)

# ==================================================
# ENABLE CORS
# ==================================================

CORS(app)

# ==================================================
# DATABASE CONFIGURATION
# ==================================================

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_PORT = os.getenv("DB_PORT", "3306")

app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# ==================================================
# INITIALIZE DATABASE
# ==================================================

db.init_app(app)

# ==================================================
# IMPORT MODELS
# ==================================================

from models.booking_model import Booking

# ==================================================
# CREATE DATABASE TABLES
# ==================================================

with app.app_context():

    db.create_all()

# ==================================================
# HOME ROUTE
# ==================================================

@app.route("/")

def home():

    return jsonify({

        "success": True,

        "message": "Makeup Artist Backend Running"

    }), 200

# ==================================================
# HEALTH CHECK ROUTE
# ==================================================

@app.route("/health")

def health():

    return jsonify({

        "status": "healthy",

        "application": "makeup-backend"

    }), 200

# ==================================================
# CREATE BOOKING API
# ==================================================

@app.route("/api/bookings", methods=["POST"])

def book_appointment():

    try:

        data = request.get_json()

        return create_booking(data)

    except Exception as error:

        print("BOOKING API ERROR:", error)

        return jsonify({

            "success": False,

            "error": str(error)

        }), 500

# ==================================================
# GET ALL BOOKINGS
# ==================================================

@app.route("/api/bookings", methods=["GET"])

def get_bookings():

    try:

        bookings = Booking.query.all()

        booking_list = []

        for booking in bookings:

            booking_list.append({

                "id": booking.id,

                "name": booking.name,

                "email": booking.email,

                "phone": booking.phone,

                "service": booking.service,

                "appointment_date": str(booking.appointment_date),

                "message": booking.message
            })

        return jsonify({

            "success": True,

            "bookings": booking_list

        }), 200

    except Exception as error:

        print("GET BOOKINGS ERROR:", error)

        return jsonify({

            "success": False,

            "error": str(error)

        }), 500

# ==================================================
# 404 ERROR HANDLER
# ==================================================

@app.errorhandler(404)

def not_found(error):

    return jsonify({

        "success": False,

        "message": "Route Not Found"

    }), 404

# ==================================================
# 500 ERROR HANDLER
# ==================================================

@app.errorhandler(500)

def internal_error(error):

    return jsonify({

        "success": False,

        "message": "Internal Server Error"

    }), 500

# ==================================================
# RUN APPLICATION
# ==================================================

if __name__ == "__main__":

    app.run(

        host="0.0.0.0",

        port=5000,

        debug=True
    )
