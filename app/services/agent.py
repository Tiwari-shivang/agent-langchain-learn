from app.agent.agentConfig import llm
from app.schemas.agent import QueryRequest, AgentResponse

class AgentService:
    def __init__(self):
        pass

    def chat_agent(self, request: QueryRequest) -> AgentResponse:
        agent_response = llm.invoke(request.query)
        response = AgentResponse(answer=agent_response.content)
        return response
