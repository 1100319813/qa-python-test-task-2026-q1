import allure
from app.client import ApiClient


class PetApi:
    def __init__(self, client: ApiClient) -> None:
        self.client = client

    @allure.step("Create pet")
    async def create_pet(self, payload: dict):
        return await self.client.post("/pet", json=payload)

    @allure.step("Update pet")
    async def update_pet(self, payload: dict):
        return await self.client.put("/pet", json=payload)

    @allure.step("Get pet by id: {pet_id}")
    async def get_pet(self, pet_id: int):
        return await self.client.get(f"/pet/{pet_id}")

    @allure.step("Delete pet by id: {pet_id}")
    async def delete_pet(self, pet_id: int):
        return await self.client.delete(f"/pet/{pet_id}")

    @allure.step("Find pets by status: {status}")
    async def find_by_status(self, status: str):
        return await self.client.get("/pet/findByStatus", params={"status": status})

    @allure.step("Find pets by tags: {tags}")
    async def find_by_tags(self, tags: list[str]):
        return await self.client.get("/pet/findByTags", params=[("tags", tag) for tag in tags])