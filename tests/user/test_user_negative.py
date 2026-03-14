import pytest
import allure


@allure.epic("Petstore API")
@allure.feature("User")
@allure.story("Negative scenarios")
@allure.title("Get nonexistent user by username")
@pytest.mark.asyncio
@pytest.mark.user
@pytest.mark.negative
async def test_get_nonexistent_user(user_api):
    response = await user_api.get_user("no_such_user_123456789")

    assert response.status_code in (400, 404)


@allure.epic("Petstore API")
@allure.feature("User")
@allure.story("Negative scenarios")
@allure.title("Delete nonexistent user by username")
@pytest.mark.asyncio
@pytest.mark.user
@pytest.mark.negative
async def test_delete_nonexistent_user(user_api):
    response = await user_api.delete_user("no_such_user_123456789")

    assert response.status_code in (200, 400, 404)