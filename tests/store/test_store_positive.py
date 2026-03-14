import pytest
import allure

from app.utils.data_factory import pet_payload, order_payload


@allure.epic("Petstore API")
@allure.feature("Store")
@allure.story("Positive scenarios")
@allure.title("Get store inventory")
@pytest.mark.asyncio
@pytest.mark.store
@pytest.mark.regression
async def test_get_inventory(store_api):
    response = await store_api.get_inventory()

    assert response.status_code == 200
    assert isinstance(response.json(), dict)


@allure.epic("Petstore API")
@allure.feature("Store")
@allure.story("Positive scenarios")
@allure.title("Create, get and delete order")
@pytest.mark.asyncio
@pytest.mark.store
@pytest.mark.regression
async def test_create_get_delete_order(store_api, pet_api):
    pet = pet_payload()
    order = order_payload(pet["id"])

    await pet_api.create_pet(pet)

    try:
        create_response = await store_api.create_order(order)
        assert create_response.status_code == 200

        created_body = create_response.json()
        assert created_body["id"] == order["id"]
        assert created_body["petId"] == order["petId"]
        assert created_body["quantity"] == order["quantity"]
        assert created_body["status"] == order["status"]

        get_response = await store_api.get_order(order["id"])
        assert get_response.status_code == 200

        get_body = get_response.json()
        assert get_body["id"] == order["id"]
        assert get_body["petId"] == order["petId"]
        assert get_body["status"] == order["status"]

    finally:
        delete_order_response = await store_api.delete_order(order["id"])
        assert delete_order_response.status_code in (200, 404)

        delete_pet_response = await pet_api.delete_pet(pet["id"])
        assert delete_pet_response.status_code in (200, 404)