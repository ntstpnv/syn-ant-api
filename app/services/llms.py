from langchain_ollama import ChatOllama

from app.settings import SETTINGS


def get_llm() -> ChatOllama:
    """
    :return: экземпляр языковой модели с параметрами:
        model: название языковой модели
        base_url: адрес сервера
        temperature: уровень креатива в ответах
    """

    return ChatOllama(
        model=SETTINGS.MODEL,
        base_url=SETTINGS.BASE_URL,
        temperature=0,
    )
