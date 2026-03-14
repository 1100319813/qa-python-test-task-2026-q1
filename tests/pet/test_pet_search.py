import pytest
import allure
import asyncio

from app.utils.data_factory import pet_payload


@allure.epic("Petstore API")
@allure.feature("Pet")
@allure.story("Search")
@allure.title("Find pets by status")
@pytest.mark.asyncio
@pytest.mark.pet
@pytest.mark.e2e
async def test_find_pets_by_status(pet_api):
    pets = [pet_payload(status="available") for _ in range(3)]

    await asyncio.gather(*(pet_api.create_pet(p) for p in pets))

    try:
        response = await pet_api.find_by_status("available")
        assert response.status_code == 200

        body = response.json()

        returned_ids = {pet["id"] for pet in body}
        created_ids = {pet["id"] for pet in pets}

        assert created_ids.issubset(returned_ids)

    finally:
        await asyncio.gather(*(pet_api.delete_pet(p["id"]) for p in pets))
 
 
        
@allure.epic("Petstore API")
@allure.feature("Pet")
@allure.story("Search")
@allure.title("Find pets by tags")
@pytest.mark.asyncio
@pytest.mark.pet
async def test_find_pets_by_tags(pet_api):
    pet = pet_payload()

    pet["tags"] = [
        {
            "id": pet["id"],
            "name": "test_tag"
        }
    ]

    await pet_api.create_pet(pet)

    try:
        response = await pet_api.find_by_tags(["test_tag"])
        assert response.status_code == 200

        body = response.json()

        returned_ids = {p["id"] for p in body}

        assert pet["id"] in returned_ids

    finally:
        await pet_api.delete_pet(pet["id"])