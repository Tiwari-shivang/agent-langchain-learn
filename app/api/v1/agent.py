from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from app.schemas.agent import AgentResponse, QueryRequest
from app.services.services import get_agent_service
from app.services.agent import AgentService

router = APIRouter()

@router.post("/query")
async def agent_chat(payload: QueryRequest, agentService: AgentService = Depends(get_agent_service)) -> StreamingResponse:
    async def generate():
        async for chunk in agentService.chat_agent(payload):
            yield chunk
    return StreamingResponse(generate(), media_type="texttext/plain")