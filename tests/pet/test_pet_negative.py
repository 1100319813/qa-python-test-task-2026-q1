import pytest
import allure


@allure.epic("Petstore API")
@allure.feature("Pet")
@allure.story("Negative scenarios")
@allure.title("Get nonexistent pet by id")
@pytest.mark.asyncio
@pytest.mark.pet
@pytest.mark.negative
async def test_get_nonexistent_pet(pet_api):
    response = await pet_api.get_pet(999999999999)

    assert response.status_code in (400, 404)


@allure.epic("Petstore API")
@allure.feature("Pet")
@allure.story("Negative scenarios")
@allure.title("Delete nonexistent pet by id")
@pytest.mark.asyncio
@pytest.mark.pet
@pytest.mark.negative
async def test_delete_nonexistent_pet(pet_api):
    response = await pet_api.delete_pet(999999999999)

    assert response.status_code in (200, 400, 404)