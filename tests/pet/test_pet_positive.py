import pytest
import allure

from app.utils.data_factory import pet_payload


@allure.epic("Petstore API")
@allure.feature("Pet")
@allure.story("Positive scenarios")
@allure.title("Create, get and delete pet")
@pytest.mark.asyncio
@pytest.mark.pet
@pytest.mark.regression
async def test_create_get_delete_pet(pet_api):
    payload = pet_payload()

    try:
        create_response = await pet_api.create_pet(payload)
        assert create_response.status_code == 200

        created_body = create_response.json()
        assert created_body["id"] == payload["id"]
        assert created_body["name"] == payload["name"]
        assert created_body["status"] == payload["status"]

        get_response = await pet_api.get_pet(payload["id"])
        assert get_response.status_code == 200

        get_body = get_response.json()
        assert get_body["id"] == payload["id"]
        assert get_body["name"] == payload["name"]
        assert get_body["status"] == payload["status"]

    finally:
        delete_response = await pet_api.delete_pet(payload["id"])
        assert delete_response.status_code in (200, 404)