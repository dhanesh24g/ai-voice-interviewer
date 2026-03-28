from pydantic import BaseModel, HttpUrl

from app.schemas.common import TimestampResponse


class JobTargetCreate(BaseModel):
    job_posting_url: HttpUrl


class JobTargetExtractRequest(BaseModel):
    job_posting_url: HttpUrl


class JobTargetResponse(TimestampResponse):
    id: int
    job_posting_url: str
    company_name: str | None = None
    role_title: str | None = None
    job_description: str | None = None
    extraction_confidence: float | None = None
    raw_tinyfish_result: dict | None = None
    raw_page_text: str | None = None
    status: str
