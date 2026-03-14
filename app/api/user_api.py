import allure
from app.client import ApiClient


class UserApi:
    def __init__(self, client: ApiClient) -> None:
        self.client = client

    @allure.step("Create user")
    async def create_user(self, payload: dict):
        return await self.client.post("/user", json=payload)

    @allure.step("Create users with list")
    async def create_users_with_list(self, payload: list[dict]):
        return await self.client.post("/user/createWithList", json=payload)

    @allure.step("Login user: {username}")
    async def login(self, username: str, password: str):
        return await self.client.get(
            "/user/login",
            params={"username": username, "password": password},
        )

    @allure.step("Logout user")
    async def logout(self):
        return await self.client.get("/user/logout")

    @allure.step("Get user by username: {username}")
    async def get_user(self, username: str):
        return await self.client.get(f"/user/{username}")

    @allure.step("Update user: {username}")
    async def update_user(self, username: str, payload: dict):
        return await self.client.put(f"/user/{username}", json=payload)

    @allure.step("Delete user: {username}")
    async def delete_user(self, username: str):
        return await self.client.delete(f"/user/{username}")