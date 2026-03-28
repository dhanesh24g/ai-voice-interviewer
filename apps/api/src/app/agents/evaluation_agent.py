from __future__ import annotations

from app.providers.llm_provider import LLMProvider


class EvaluationAgent:
    def __init__(self, llm: LLMProvider) -> None:
        self.llm = llm

    def evaluate_answer(self, question: str, answer: str, job_description: str) -> dict:
        return self.llm.evaluate_answer(question=question, answer=answer, job_description=job_description)

    def generate_report(self, transcript: str, evaluations: list[dict]) -> dict:
        return self.llm.generate_feedback(transcript=transcript, evaluations=evaluations)
