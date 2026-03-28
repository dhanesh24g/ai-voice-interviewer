from app.schemas.common import TimestampResponse


class QuestionResponse(TimestampResponse):
    id: int
    job_target_id: int
    source_id: int | None = None
    text: str
    category: str | None = None
    frequency_score: float
    recency_score: float
    relevance_score: float
    importance_score: float
    final_score: float
    rationale: str | None = None
    is_fallback: bool
