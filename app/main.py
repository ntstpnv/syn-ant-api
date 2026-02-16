from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

from app.core import graphs, states
from app.schemas import Request, Response


app = FastAPI()


def common_request(request: Request, _type: str) -> Response:
    """
    Алгоритм:

    Валидировать данные от пользователя
    Инициализировать начальное состояние графа
    Запустить граф (syn/ant - split - END)
    Проверить наличие ошибок
    Вернуть полученный данные
    """

    if _type not in {"syn", "ant"}:
        raise HTTPException(
            status_code=422,
            detail="Ошибка: Неверные входные данные",
        )

    start = states.State(
        request=request,
        type=_type,
    )

    try:
        results = graphs.graph.invoke(start)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Ошибка(сервер): {str(e)}",
        )

    try:
        finish = states.State(**results)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Ошибка(целостность данных): {str(e)}",
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


@app.get("/", response_class=HTMLResponse)
def root():
    return '<html><body><a href="/docs">Swagger</a></body></html>'


@app.post("/api/syn/", response_model=Response)
async def get_synonyms(request: Request):
    return common_request(request, "syn")


@app.post("/api/ant/", response_model=Response)
async def get_antonyms(request: Request):
    return common_request(request, "ant")
