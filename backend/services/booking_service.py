from database.db import get_connection

from utils.logger import setup_logger

import boto3
import os

logger = setup_logger()

sns = boto3.client('sns', region_name=os.getenv("AWS_REGION"))

def create_booking(data):

    try:

        connection = get_connection()

        cursor = connection.cursor()

        query = """
        INSERT INTO bookings
        (name, email, phone, booking_date, service)
        VALUES (%s, %s, %s, %s, %s)
        """

        values = (
            data['name'],
            data['email'],
            data['phone'],
            data['date'],
            data['service']
        )

        cursor.execute(query, values)

        connection.commit()

        # SNS Notification
        sns.publish(
            TopicArn=os.getenv("SNS_TOPIC_ARN"),
            Subject="New Booking",
            Message=f"""
            New Booking Received

            Name: {data['name']}
            Email: {data['email']}
            Phone: {data['phone']}
            Service: {data['service']}
            """
        )

        logger.info("Booking created successfully")

        return {
            "message": "Booking created successfully"
        }

    except Exception as e:

        logger.error(str(e))

        return {
            "error": str(e)
        }

    finally:

        cursor.close()
        connection.close()
