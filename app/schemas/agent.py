from pydantic import BaseModel, ConfigDict

class QueryRequest(BaseModel):
    query: str

class AgentResponse(BaseModel):
    answer: str
    model_config = ConfigDict(from_attributes=True)