import pytest_asyncio
from app.client import ApiClient
from app.api.pet_api import PetApi
from app.api.store_api import StoreApi
from app.api.user_api import UserApi


@pytest_asyncio.fixture
async def api_client():
    client = ApiClient()
    yield client
    await client.close()


@pytest_asyncio.fixture
async def pet_api(api_client):
    return PetApi(api_client)


@pytest_asyncio.fixture
async def store_api(api_client):
    return StoreApi(api_client)


@pytest_asyncio.fixture
async def user_api(api_client):
    return UserApi(api_client)