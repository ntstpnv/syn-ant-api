from langgraph.graph import END, StateGraph
from langgraph.graph.state import CompiledStateGraph

from app.core import nodes, states


def graph_builder() -> CompiledStateGraph:
    """
    Алгоритм:

    Создать граф с универсальным состоянием
    Добавить в граф ноды
    Задать последовательность действий
    Скомпилировать полученный граф
    """

    workflow = StateGraph(states.State)

    workflow.add_node("request", nodes.request_node)
    workflow.add_node("split", nodes.split_node)

    workflow.set_entry_point("request")
    workflow.add_edge("request", "split")
    workflow.add_edge("split", END)

    return workflow.compile()


graph = graph_builder()
