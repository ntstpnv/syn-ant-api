from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Алгоритм:

    Найти файл .env в корневой директории проекта (env_file=".env")
    Установить кодировку для корректного чтения файла .env (env_file_encoding="utf-8")
    Загрузить переменные окружения из файла .env
    Проверить, что переменная MODEL является строкой
    Проверить, что переменная BASE_URL является строкой
    Проигнорировать остальные переменные окружения (extra="ignore")

    Аттрибуты:

    MODEL - название языковой модели
    BASE_URL - адрес сервера для подключения
    """

    MODEL: str = "gemma3:4b"
    BASE_URL: str = "http://127.0.0.1:11434"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
