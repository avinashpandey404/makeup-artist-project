import boto3
import os

sns = boto3.client(
    'sns',
    region_name=os.getenv("AWS_REGION")
)

TOPIC_ARN = os.getenv("SNS_TOPIC_ARN")


def send_booking_confirmation(name, phone):

    message = f"""
Hello {name},

Your makeup appointment booking has been received successfully.

We will contact you shortly.

Thank You.
"""

    sns.publish(

        TopicArn=TOPIC_ARN,

        Message=message,

        Subject="Appointment Confirmation"
    )
