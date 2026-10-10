from fastapi import APIRouter
from app.schemas.agent import AgentResponse, QueryRequest

router = APIRouter()

@router.post("/query")
def agent_chat(payload: QueryRequest) -> AgentResponse:
    response = AgentResponse(answer=f"Static agent response {payload.query}")
    return response