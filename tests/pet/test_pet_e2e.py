import pytest
import allure

from app.utils.data_factory import pet_payload


@allure.epic("Petstore API")
@allure.feature("Pet")
@allure.story("E2E scenarios")
@allure.title("Pet lifecycle: create, get, update, verify, delete")
@pytest.mark.asyncio
@pytest.mark.pet
@pytest.mark.e2e
async def test_pet_lifecycle(pet_api):
    payload = pet_payload(status="available")

    create_response = await pet_api.create_pet(payload)
    assert create_response.status_code == 200

    get_response = await pet_api.get_pet(payload["id"])
    assert get_response.status_code == 200
    assert get_response.json()["id"] == payload["id"]

    payload["name"] = f"{payload['name']}-updated"
    payload["status"] = "sold"

    update_response = await pet_api.update_pet(payload)
    assert update_response.status_code == 200

    get_updated_response = await pet_api.get_pet(payload["id"])
    assert get_updated_response.status_code == 200

    updated_body = get_updated_response.json()
    assert updated_body["id"] == payload["id"]
    assert updated_body["name"] == payload["name"]
    assert updated_body["status"] == "sold"

    delete_response = await pet_api.delete_pet(payload["id"])
    assert delete_response.status_code == 200

    get_deleted_response = await pet_api.get_pet(payload["id"])
    assert get_deleted_response.status_code in (400, 404)