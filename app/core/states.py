from pydantic import BaseModel

from app.schemas import Request


class State(BaseModel):
    """
    Универсальное состояние графа обработки запроса

    :ivar request: запрос пользователя
    :ivar response: ответ языковой модели
    :ivar words: список полученных слов
    :ivar error: сообщение об ошибке
    """

    request: Request
    response: str = ""
    words: list[str] = []
    error: str = ""
