from flask import jsonify
from database.db import db
from models.booking_model import Booking
from services.sns_service import send_booking_confirmation


def create_booking(data):

    try:

        name = data.get("name")
        email = data.get("email")
        phone = data.get("phone")
        service = data.get("service")
        appointment_date = data.get("appointment_date")
        message = data.get("message")

        # Validation

        if not name:
            return jsonify({
                "error": "Name is required"
            }), 400

        if not email:
            return jsonify({
                "error": "Email is required"
            }), 400

        if not phone:
            return jsonify({
                "error": "Phone is required"
            }), 400

        if not service:
            return jsonify({
                "error": "Service is required"
            }), 400

        if not appointment_date:
            return jsonify({
                "error": "Appointment date is required"
            }), 400

        # Create Booking Object

        new_booking = Booking(

            name=name,
            email=email,
            phone=phone,
            service=service,
            appointment_date=appointment_date,
            message=message
        )

        # Save Into Database

        db.session.add(new_booking)

        db.session.commit()

        # Send SNS Confirmation

        send_booking_confirmation(name, phone)

        return jsonify({

            "success": True,

            "message": "Appointment booked successfully"

        }), 201

    except Exception as error:

        db.session.rollback()

        print("BOOKING ERROR:", error)

        return jsonify({

            "success": False,

            "error": str(error)

        }), 500
