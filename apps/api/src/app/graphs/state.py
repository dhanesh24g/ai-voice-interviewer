from __future__ import annotations

from typing import TypedDict


class InterviewGraphState(TypedDict, total=False):
    job_target_id: int
    job_posting_url: str
    extracted_job_metadata: dict
    raw_tinyfish_job_extraction_output: dict
    raw_research_documents: list[dict]
    question_bank: list[dict]
    interview_session_state: dict
    answers: list[dict]
    evaluations: list[dict]
    final_report: dict
