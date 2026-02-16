from app.core.states import State
from app.services import llms, prompts


llm = llms.get_llm()


def _call_llm(state: State, _type: str) -> State:
    """
    Алгоритм:

    Взять данные запроса пользователя из состояния графа
    Взять тип запроса из path params эндпоинта
    Подставить полученные данные в шаблон промта
    Сформированный промт отпправить в языковую модель
    Получить ответ и сохранить его в состоянии графа
    Вернуть состояние графа
    """

    state.response = llm.invoke(
        prompts.PROMPT.format_messages(
            word=state.request.word,
            type=_type,
        )
    ).content

    return state


def syn_node(state: State) -> State:
    return _call_llm(state, "синонимов")


def ant_node(state: State) -> State:
    return _call_llm(state, "антонимов")


def split_node(state: State) -> State:
    """
    Алгоритм:

    Взять данные ответа языковой модели из состояния графа
    Разделить строку по пробелам и сформировать список
    Сохранить полученный список в состоянии графа
    При возникновении ошибки, сохранить ее в состоянии графа
    Вернуть состояние графа
    """

    words = state.response.split()

    if len(words) == 10:
        state.words = words
    else:
        state.error = "Ошибка: Неверный формат ответа"

    return state
