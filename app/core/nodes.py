from app.core import states
from app.services import llms, prompts


llm = llms.get_llm()


def request_node(state: states.State) -> states.State:
    """
    Алгоритм:

    Взять данные запроса пользователя из состояния графа
    Подставить полученные данные в шаблон промта
    Сформированный промт отпправить в языковую модель
    Получить ответ и сохранить его в состоянии графа
    """

    state.response = llm.invoke(
        prompts.PROMPT.format_messages(
            word=state.request.word,
            type="синонимов" if state.request.type == "syn" else "антонимов",
        )
    ).content

    return state


def split_node(state: states.State) -> states.State:
    """
    Алгоритм:

    Взять данные ответа языковой модели из состояния графа
    Разделить строка по пробелам и сформировать список
    Сохранить полученный список в состоянии графа
    При возникновении ошибки, сохранить ее в состоянии графа
    """

    words = state.response.split()

    if len(words) == 10:
        state.words = words
    else:
        state.error = "Ошибка: Неверный формат ответа"

    return state
