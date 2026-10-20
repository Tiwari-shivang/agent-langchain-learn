from langchain_openai import ChatOpenAI
from openai import AsyncOpenAI
from app.core.settings import Settings, get_settings

settings: Settings = get_settings()

# 1. Custom OpenAI Async client banayein jisme ngrok header ho
custom_async_openai_client = AsyncOpenAI(
    api_key=settings.LLM_API_KEY,
    base_url=settings.LLM_BASE_URL,
    default_headers={
        "ngrok-skip-browser-warning": "true"
    }
)

# 2. ChatOpenAI ko yeh client pass kar dein
llm = ChatOpenAI(
    model=settings.LLM_MODEL,
    temperature=settings.LLM_TEMP,
    async_client=custom_async_openai_client
)