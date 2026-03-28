from __future__ import annotations

from sqlalchemy.orm import Session

from app.agents.job_extraction_agent import JobExtractionAgent
from app.services.repositories import JobTargetRepository


class JobService:
    def __init__(self, db: Session, agent: JobExtractionAgent) -> None:
        self.db = db
        self.agent = agent
        self.repo = JobTargetRepository(db)

    def create_job_target(self, url: str):
        return self.repo.create(url)

    def extract_job_target(self, url: str):
        job_target = self.repo.create(url)
        fetched = self.agent.fetch_job_posting_with_tinyfish(url)
        metadata = self.agent.extract_job_metadata(url=url, raw_text=fetched["text"])
        return self.repo.update_extraction(
            job_target,
            {
                "company_name": metadata.get("company_name"),
                "role_title": metadata.get("role_title"),
                "job_description": metadata.get("job_description"),
                "confidence": metadata.get("confidence"),
                "raw_tinyfish_result": fetched["raw"],
                "raw_page_text": fetched["text"],
                "status": "extracted",
            },
        )

    def get_job_target(self, job_target_id: int):
        return self.repo.get(job_target_id)
