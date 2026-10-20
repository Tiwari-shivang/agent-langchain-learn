from app.agent.agentConfig import llm
from app.schemas.agent import QueryRequest, AgentResponse

class AgentService:
    def __init__(self):
        pass

    async def chat_agent(self, request: QueryRequest):
        async for chunk in llm.astream(request.query):
            if chunk.content:
                yield chunk.content
