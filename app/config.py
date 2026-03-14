from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    base_url: str = "http://localhost:8080/api/v3"
    timeout: float = 10.0


settings = Settings()