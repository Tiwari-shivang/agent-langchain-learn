from fastapi import APIRouter, Depends
from app.schemas.agent import AgentResponse, QueryRequest
from app.services.services import get_agent_service
from app.services.agent import AgentService

router = APIRouter()

@router.post("/query")
def agent_chat(payload: QueryRequest, agentService: AgentService = Depends(get_agent_service)) -> AgentResponse:
    agent_response: AgentResponse = agentService.chat_agent(payload)
    return agent_response