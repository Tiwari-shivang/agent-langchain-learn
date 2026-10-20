from langchain_openai import ChatOpenAI
from app.core.settings import Settings, get_settings

settings: Settings = get_settings()

llm = ChatOpenAI(
    model=settings.LLM_MODEL,
    temperature=settings.LLM_TEMP,
    api_key=settings.LLM_API_KEY,
    base_url=settings.LLM_BASE_URL
)