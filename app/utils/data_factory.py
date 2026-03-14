import random
import time


def unique_id() -> int:
    return int(time.time() * 1000) + random.randint(1, 999)


def pet_payload(status: str = "available", tag_name: str = "test-tag") -> dict:
    pet_id = unique_id()
    return {
        "id": pet_id,
        "name": f"pet-{pet_id}",
        "category": {"id": 1, "name": "dogs"},
        "photoUrls": ["https://example.com/photo.jpg"],
        "tags": [{"id": 1, "name": tag_name}],
        "status": status,
    }


def user_payload() -> dict:
    uid = unique_id()
    return {
        "id": uid,
        "username": f"user_{uid}",
        "firstName": "Test",
        "lastName": "User",
        "email": f"user_{uid}@example.com",
        "password": "Password123!",
        "phone": "1234567890",
        "userStatus": 1,
    }


def order_payload(pet_id: int) -> dict:
    oid = unique_id()
    return {
        "id": oid,
        "petId": pet_id,
        "quantity": 1,
        "shipDate": "2026-03-13T10:00:00.000Z",
        "status": "placed",
        "complete": True,
    }