from app.schemas.common import TimestampResponse


class SourceResponse(TimestampResponse):
    id: int
    job_target_id: int
    source_url: str
    source_type: str
    raw_tinyfish_result: dict | None = None
    parsed_text: str | None = None
    fetch_status: str
