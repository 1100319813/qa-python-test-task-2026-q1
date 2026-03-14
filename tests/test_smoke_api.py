import pytest


@pytest.mark.asyncio
async def test_inventory_smoke(store_api):
    response = await store_api.get_inventory()

    assert response.status_code == 200
    assert isinstance(response.json(), dict)