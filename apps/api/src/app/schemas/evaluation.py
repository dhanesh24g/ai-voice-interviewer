from datetime import datetime

from pydantic import BaseModel

from app.schemas.common import ORMBaseModel


class EvaluationRunRequest(BaseModel):
    job_target_id: int | None = None
    session_id: int | None = None
    run_type: str = "system_check"


class EvaluationResponse(ORMBaseModel):
    id: int
    session_id: int
    turn_id: int | None = None
    score: float
    strengths: list[str]
    weaknesses: list[str]
    missing_points: list[str]
    suggestion: str | None = None
    created_at: datetime


class FeedbackReportResponse(ORMBaseModel):
    id: int
    session_id: int
    summary: str
    overall_score: float
    strengths: list[str]
    improvement_areas: list[str]
    prep_guidance: list[str]
    created_at: datetime


class EvaluationRunResponse(ORMBaseModel):
    id: int
    run_type: str
    status: str
    metrics: dict | None = None
    notes: str | None = None
    created_at: datetime
