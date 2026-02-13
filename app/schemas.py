from typing import Literal

from pydantic import BaseModel


class Request(BaseModel):
    """
    Запрос пользователя

    :ivar word: исходное слово на русском языке
    :ivar type: искать синонимы или антонимы
    """

    word: str
    type: Literal["syn", "ant"]


class Response(BaseModel):
    """
    Ответ языковой модели

    :ivar words: список найденных слов заданного типа
    """

    words: list[str]
