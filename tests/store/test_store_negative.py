import pytest
import allure


@allure.epic("Petstore API")
@allure.feature("Store")
@allure.story("Negative scenarios")
@allure.title("Get nonexistent order by id")
@pytest.mark.asyncio
@pytest.mark.store
@pytest.mark.negative
async def test_get_nonexistent_order(store_api):
    response = await store_api.get_order(999999999999)

    assert response.status_code in (400, 404)


@allure.epic("Petstore API")
@allure.feature("Store")
@allure.story("Negative scenarios")
@allure.title("Delete nonexistent order by id")
@pytest.mark.asyncio
@pytest.mark.store
@pytest.mark.negative
async def test_delete_nonexistent_order(store_api):
    response = await store_api.delete_order(999999999999)

    assert response.status_code in (200, 400, 404)