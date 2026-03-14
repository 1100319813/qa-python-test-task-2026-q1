import asyncio
import pytest
import allure

from app.utils.data_factory import pet_payload
from app.utils.data_factory import user_payload


@allure.epic("Petstore API")
@allure.feature("Async demo")
@allure.story("Parallel operations")
@allure.title("Parallel create, check and delete pets")
@pytest.mark.asyncio
@pytest.mark.async_demo
@pytest.mark.regression
async def test_parallel_create_and_check_pets(pet_api):
    pets = [pet_payload(status="available") for _ in range(3)]

    await asyncio.gather(*(pet_api.create_pet(pet) for pet in pets))

    try:
        responses = await asyncio.gather(*(pet_api.get_pet(pet["id"]) for pet in pets))

        for response, pet in zip(responses, pets):
            assert response.status_code == 200
            assert response.json()["id"] == pet["id"]
    finally:
        await asyncio.gather(*(pet_api.delete_pet(pet["id"]) for pet in pets))
        
        
@allure.epic("Petstore API")
@allure.feature("Async demo")
@allure.story("Parallel user operations")
@allure.title("Parallel create, check and delete users")
@pytest.mark.asyncio
@pytest.mark.async_demo
@pytest.mark.user
@pytest.mark.regression
async def test_parallel_create_and_check_users(user_api):
    users = [user_payload() for _ in range(3)]

    await asyncio.gather(*(user_api.create_user(user) for user in users))

    try:
        responses = await asyncio.gather(
            *(user_api.get_user(user["username"]) for user in users)
        )

        for response, user in zip(responses, users):
            assert response.status_code == 200
            assert response.json()["username"] == user["username"]
    finally:
        await asyncio.gather(
            *(user_api.delete_user(user["username"]) for user in users)
        )