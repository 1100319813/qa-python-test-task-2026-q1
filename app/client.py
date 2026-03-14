import httpx
from app.config import settings


class ApiClient:
    def __init__(self) -> None:
        self._client = httpx.AsyncClient(
            base_url=settings.base_url,
            timeout=settings.timeout,
            headers={"Content-Type": "application/json", "accept": "application/json"},
        )

    async def get(self, url: str, **kwargs):
        return await self._client.get(url, **kwargs)

    async def post(self, url: str, **kwargs):
        return await self._client.post(url, **kwargs)

    async def put(self, url: str, **kwargs):
        return await self._client.put(url, **kwargs)

    async def delete(self, url: str, **kwargs):
        return await self._client.delete(url, **kwargs)

    async def close(self):
        await self._client.aclose()