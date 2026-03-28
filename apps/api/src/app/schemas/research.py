from pydantic import BaseModel

from app.schemas.question import QuestionResponse
from app.schemas.source import SourceResponse


class ResearchRunRequest(BaseModel):
    job_target_id: int
    stream: bool = False


class ResearchRunResponse(BaseModel):
    job_target_id: int
    sources: list[SourceResponse]
    questions: list[QuestionResponse]
