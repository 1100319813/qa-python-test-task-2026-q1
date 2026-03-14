import pytest
import allure

from app.utils.data_factory import user_payload


@allure.epic("Petstore API")
@allure.feature("User")
@allure.story("Positive scenarios")
@allure.title("Create users with list and verify they are available")
@pytest.mark.asyncio
@pytest.mark.user
@pytest.mark.regression
async def test_create_users_with_list(user_api):
    users = [user_payload() for _ in range(2)]

    try:
        create_response = await user_api.create_users_with_list(users)
        assert create_response.status_code == 200

        for user in users:
            get_response = await user_api.get_user(user["username"])
            assert get_response.status_code == 200

            body = get_response.json()
            assert body["username"] == user["username"]
            assert body["email"] == user["email"]
            assert body["id"] == user["id"]

    finally:
        for user in users:
            delete_response = await user_api.delete_user(user["username"])
            assert delete_response.status_code in (200, 404)