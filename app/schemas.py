from pydantic import BaseModel


class Request(BaseModel):
    """
    Запрос пользователя:

    word - исходное слово на русском языке
    """

    word: str


class Response(BaseModel):
    """
    Ответ языковой модели:

    words - список найденных слов заданного типа
    """

    words: list[str]
