import pytest
import allure

from app.utils.data_factory import user_payload, pet_payload, order_payload


@allure.epic("Petstore API")
@allure.feature("User")
@allure.story("E2E scenarios")
@allure.title("Full user scenario: create user, login, create order, get order, delete order, delete user")
@pytest.mark.asyncio
@pytest.mark.user
@pytest.mark.store
@pytest.mark.e2e
async def test_full_user_flow(user_api, pet_api, store_api):
    user = user_payload()
    pet = pet_payload()
    order = order_payload(pet["id"])

    await user_api.create_user(user)
    await pet_api.create_pet(pet)

    try:
        login_response = await user_api.login(user["username"], user["password"])
        assert login_response.status_code == 200

        create_order_response = await store_api.create_order(order)
        assert create_order_response.status_code == 200

        get_order_response = await store_api.get_order(order["id"])
        assert get_order_response.status_code == 200

        get_order_body = get_order_response.json()
        assert get_order_body["id"] == order["id"]
        assert get_order_body["petId"] == pet["id"]

        delete_order_response = await store_api.delete_order(order["id"])
        assert delete_order_response.status_code == 200

        get_deleted_order_response = await store_api.get_order(order["id"])
        assert get_deleted_order_response.status_code in (400, 404)

    finally:
        delete_pet_response = await pet_api.delete_pet(pet["id"])
        assert delete_pet_response.status_code in (200, 404)

        delete_user_response = await user_api.delete_user(user["username"])
        assert delete_user_response.status_code in (200, 404)