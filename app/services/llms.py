from langchain_ollama import ChatOllama

from app.settings import settings


def get_llm() -> ChatOllama:
    """
    Фабрика экземпляров языковой модели с параметрами:

    model - название языковой модели
    base_url - адрес сервера для подключения
    temperature - уровень креатива в ответах
    """

    return ChatOllama(
        model=settings.MODEL,
        base_url=settings.BASE_URL,
        temperature=0,
    )
