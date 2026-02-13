from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Данные подключения к языковой модели

    :ivar MODEL: название модели
    :ivar BASE_URL: адрес сервера
    """

    MODEL: str = "gemma3:4b"
    BASE_URL: str = "http://127.0.0.1:11434"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


SETTINGS = Settings()
