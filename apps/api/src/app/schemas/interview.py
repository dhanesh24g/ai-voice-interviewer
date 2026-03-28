from datetime import datetime
from typing import Literal

from pydantic import BaseModel

from app.schemas.common import ORMBaseModel


class InterviewSessionStartRequest(BaseModel):
    job_target_id: int
    mode: Literal["text", "voice"] = "text"


class InterviewSessionEventRequest(BaseModel):
    event_type: Literal["user_text", "user_audio_chunk", "clarification_request", "stop_interview"]
    payload: str | None = None


class InterviewTurnResponse(ORMBaseModel):
    id: int
    question_id: int | None
    turn_index: int
    agent_prompt: str
    user_response: str | None = None
    event_type: str
    created_at: datetime


class InterviewSessionResponse(ORMBaseModel):
    id: int
    job_target_id: int
    status: str
    mode: str
    current_question_index: int
    stop_reason: str | None = None
    started_at: datetime
    ended_at: datetime | None = None
    turns: list[InterviewTurnResponse]
