from typing import Literal

from pydantic import BaseModel

from app.schemas import Request


class State(BaseModel):
    """
    Универсальное состояние графа обработки запроса

    Аттрибуты:

    request - запрос пользователя
    type - ищем синонимы или антонимы
    response - строковый ответ языковой модели
    words - список полученных слов
    error - сообщение об ошибке
    """

    request: Request
    type: Literal["syn", "ant"]
    response: str = ""
    words: list[str] = []
    error: str = ""
