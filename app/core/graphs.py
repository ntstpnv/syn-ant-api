from langgraph.graph import END, StateGraph
from langgraph.graph.state import CompiledStateGraph

from app.core import nodes, states


def graph_builder() -> CompiledStateGraph:
    """
    Алгоритм:

    Создать граф с универсальным состоянием
    Добавить в граф ноды
    Определить начальную ноду
    Задать последовательность переходов
    Скомпилировать полученный граф
    """

    workflow = StateGraph(states.State)

    workflow.add_node("syn", nodes.syn_node)
    workflow.add_node("ant", nodes.ant_node)
    workflow.add_node("split", nodes.split_node)

    workflow.set_conditional_entry_point(
        lambda state: state.type,
        ["syn", "ant"],
    )

    workflow.add_edge("syn", "split")
    workflow.add_edge("ant", "split")
    workflow.add_edge("split", END)

    return workflow.compile()


graph = graph_builder()
