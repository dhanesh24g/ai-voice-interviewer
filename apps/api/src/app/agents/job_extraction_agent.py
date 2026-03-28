from __future__ import annotations

from app.providers.llm_provider import LLMProvider
from app.providers.tinyfish_provider import TinyFishProvider


class JobExtractionAgent:
    def __init__(self, tinyfish: TinyFishProvider, llm: LLMProvider) -> None:
        self.tinyfish = tinyfish
        self.llm = llm

    def fetch_job_posting_with_tinyfish(self, url: str) -> dict:
        result = self.tinyfish.fetch_page(url)
        return {"url": url, "raw": result.raw, "text": result.text, "metadata": result.metadata}

    def extract_job_metadata(self, url: str, raw_text: str) -> dict:
        return self.llm.extract_job_metadata(raw_text=raw_text, url=url)
