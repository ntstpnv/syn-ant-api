from langchain_core.prompts import ChatPromptTemplate

# ТЗ 1.2
# А есть ли какая-то возможность вот эту фразу "В ответе должны быть ТОЛЬКО все найденные слова через пробел"
# заменить на что-то, чтобы ответ от ИИ всегда был структурированным вне зависимости от текущего промпта?
# Структурированным - я подразумеваю то, что бы мы смогли этот ответ разбирать кодом без этой фразы.

# Одно из решений - PydanticOutputParser
# 1. Создать модель для строгой структуры ответа LLM
# 2. Создать экземпляр парсера, передав ему эту модель
# 3. Объявить в шаблоне промпта переменную format_instructions (место для инструкции)
# 4. Передать при сборке промпта output_parser.get_format_instructions() в качестве значения (генерирует инструкции)
# 5. Вызвать LLM и пропустить её ответ через OutputParser, чтобы получить на выходе объект класса Words с заполненными данными

# в schemas.py
# class Words(BaseModel): - например, так (1)
#     words: List[str]

# parser = PydanticOutputParser(pydantic_object=Words) - например, так (2)

TEXT = (
    "Ты эксперт по русскому языку. "
    'Твоя задача найти СТРОГО десять {type} к слову "{word}". '
    "Слова должны быть уникальными по смыслу. "
    "Слова не должны повторяться. "
    "Слова должны состоять только из одного слова. "
    "Слова должны состоять только из маленьких букв. "
    "В ответе должны быть ТОЛЬКО все найденные слова через пробел"
    # "{format_instructions}" - например, так (3)
)


PROMPT = ChatPromptTemplate.from_messages(
    [
        ("human", TEXT),
    ]
)

# в nodes.py
# state.response = llm.invoke(
#     prompts.PROMPT.format_messages(
#         word=state.request.word,
#         type=_type,
#         format_instructions=prompts.parser.get_format_instructions() - например, так (4)
#     )
# ).content

# try: - например, так (5)
#     parsed = prompts.parser.invoke(state.response)
#     state.words = parsed.words
# except Exception as e:
#     state.words = []
#     state.error = "Ошибка: с парсингом что-то не так"