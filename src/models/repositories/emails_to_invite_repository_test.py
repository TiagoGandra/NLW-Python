import pytest
import uuid
from .emails_to_invite_repository import EmailsToInviteRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason="interacao com o banco")
def test_registry_email():
    conn = db_connection_handler.get_connnection()
    emails_to_invite_repository = EmailsToInviteRepository(conn)

    emails_trips_infos = {
        "id": str(uuid.uuid4()),
        "trip_id": trip_id,
        "email": "olaMundo@email.com"
    }
    emails_to_invite_repository.registry_email(emails_trips_infos)

@pytest.mark.skip(reason="interacao com o banco")
def test_find_emails_from_trip():
    conn = db_connection_handler.get_connnection()
    emails_to_invite_repository = EmailsToInviteRepository(conn)

    emails = emails_to_invite_repository.find_email_from_trip(trip_id)
    print()
    print(emails)