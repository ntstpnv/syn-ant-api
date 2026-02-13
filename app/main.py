from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

from app.core import graphs, states
from app.schemas import Request, Response

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def root():
    return '<html><body><a href="/docs">Swagger</a></body></html>'


@app.post("/api/syn-ant/", response_model=Response)
async def get_words(request: Request):
    """
    Алгоритм:

    Валидировать данные от пользователя
    Инициализировать начальное состояние графа
    Запустить граф (request - split - END)
    Проверить наличие ошибок
    Вернуть полученный данные
    """

    start = states.State(request=request)

    try:
        results = graphs.graph.invoke(start)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Внутренняя ошибка сервера: {str(e)}",
        )

    try:
        finish = states.State(**results)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Ошибка целостности данных: {str(e)}",
        )

    if finish.error:
        raise HTTPException(
            status_code=422,
            detail=finish.error,
        )

    if not finish.words:
        raise HTTPException(
            status_code=404,
            detail="Ошибка: Поиск не дал результатов",
        )

    return Response(words=finish.words)
