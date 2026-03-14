import pytest
import allure

from app.utils.data_factory import user_payload


@allure.epic("Petstore API")
@allure.feature("User")
@allure.story("Positive scenarios")
@allure.title("Create, get and delete user")
@pytest.mark.asyncio
@pytest.mark.user
@pytest.mark.regression
async def test_create_get_delete_user(user_api):
    user = user_payload()

    try:
        create_response = await user_api.create_user(user)
        assert create_response.status_code == 200

        get_response = await user_api.get_user(user["username"])
        assert get_response.status_code == 200

        get_body = get_response.json()
        assert get_body["id"] == user["id"]
        assert get_body["username"] == user["username"]
        assert get_body["email"] == user["email"]

    finally:
        delete_response = await user_api.delete_user(user["username"])
        assert delete_response.status_code in (200, 404)


@allure.epic("Petstore API")
@allure.feature("User")
@allure.story("Positive scenarios")
@allure.title("Update existing user")
@pytest.mark.asyncio
@pytest.mark.user
@pytest.mark.regression
async def test_update_user(user_api):
    user = user_payload()

    await user_api.create_user(user)

    try:
        user["firstName"] = "UpdatedFirstName"
        user["lastName"] = "UpdatedLastName"
        user["email"] = f"updated_{user['id']}@example.com"

        update_response = await user_api.update_user(user["username"], user)
        assert update_response.status_code == 200

        get_response = await user_api.get_user(user["username"])
        assert get_response.status_code == 200

        get_body = get_response.json()
        assert get_body["firstName"] == "UpdatedFirstName"
        assert get_body["lastName"] == "UpdatedLastName"
        assert get_body["email"] == f"updated_{user['id']}@example.com"

    finally:
        delete_response = await user_api.delete_user(user["username"])
        assert delete_response.status_code in (200, 304, 404)


@allure.epic("Petstore API")
@allure.feature("User")
@allure.story("Positive scenarios")
@allure.title("Login and logout user")
@pytest.mark.asyncio
@pytest.mark.user
@pytest.mark.regression
async def test_login_logout_user(user_api):
    user = user_payload()

    await user_api.create_user(user)

    try:
        login_response = await user_api.login(user["username"], user["password"])
        assert login_response.status_code == 200

        logout_response = await user_api.logout()
        assert logout_response.status_code == 200

    finally:
        delete_response = await user_api.delete_user(user["username"])
        assert delete_response.status_code in (200, 404)