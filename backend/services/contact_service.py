from database.db import get_connection

from utils.logger import setup_logger

logger = setup_logger()

def create_contact(data):

    try:

        connection = get_connection()

        cursor = connection.cursor()

        query = """
        INSERT INTO contacts
        (name, email, message)
        VALUES (%s, %s, %s)
        """

        values = (
            data['name'],
            data['email'],
            data['message']
        )

        cursor.execute(query, values)

        connection.commit()

        logger.info("Contact saved successfully")

        return {
            "message": "Contact saved successfully"
        }

    except Exception as e:

        logger.error(str(e))

        return {
            "error": str(e)
        }

    finally:

        cursor.close()
        connection.close()
