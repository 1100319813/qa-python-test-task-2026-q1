import allure
from app.client import ApiClient


class StoreApi:
    def __init__(self, client: ApiClient) -> None:
        self.client = client

    @allure.step("Get inventory")
    async def get_inventory(self):
        return await self.client.get("/store/inventory")

    @allure.step("Create order")
    async def create_order(self, payload: dict):
        return await self.client.post("/store/order", json=payload)

    @allure.step("Get order by id: {order_id}")
    async def get_order(self, order_id: int):
        return await self.client.get(f"/store/order/{order_id}")

    @allure.step("Delete order by id: {order_id}")
    async def delete_order(self, order_id: int):
        return await self.client.delete(f"/store/order/{order_id}")