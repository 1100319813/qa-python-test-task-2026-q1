import pytest
import allure

from app.utils.data_factory import pet_payload, order_payload


@allure.epic("Petstore API")
@allure.feature("Store")
@allure.story("E2E scenarios")
@allure.title("Order lifecycle: create, get, delete")
@pytest.mark.asyncio
@pytest.mark.store
@pytest.mark.e2e
async def test_order_lifecycle(store_api, pet_api):
    pet = pet_payload()
    order = order_payload(pet["id"])

    await pet_api.create_pet(pet)

    create_response = await store_api.create_order(order)
    assert create_response.status_code == 200

    get_response = await store_api.get_order(order["id"])
    assert get_response.status_code == 200

    get_body = get_response.json()
    assert get_body["id"] == order["id"]
    assert get_body["petId"] == pet["id"]
    assert get_body["status"] == order["status"]

    delete_response = await store_api.delete_order(order["id"])
    assert delete_response.status_code == 200

    get_deleted_response = await store_api.get_order(order["id"])
    assert get_deleted_response.status_code in (400, 404)

    delete_pet_response = await pet_api.delete_pet(pet["id"])
    assert delete_pet_response.status_code in (200, 404)