import os

from notifications_python_client.notifications import NotificationsAPIClient

API_KEY = os.environ.get("NOTIFICATIONS_API_KEY")
notifications_client = NotificationsAPIClient(API_KEY)


def send_text(template_id: str, personalisation: dict):
    response = notifications_client.send_sms_notification(
        phone_number='++447435637775',
        template_id=template_id,
        personalisation=personalisation
    )
