from __future__ import annotations

from collections import OrderedDict

from app.providers.llm_provider import LLMProvider
from app.utils.scoring import compute_question_score


class QuestionAgent:
    def __init__(self, llm: LLMProvider) -> None:
        self.llm = llm

    def extract_questions(self, raw_documents: list[dict]) -> list[dict]:
        context = "\n\n".join(item.get("text", "") for item in raw_documents)
        return self.llm.extract_questions(context)

    def fallback_questions(self, company_name: str, role_title: str, job_description: str) -> list[dict]:
        questions = self.llm.infer_questions_from_jd(company_name, role_title, job_description)
        for item in questions:
            item["is_fallback"] = True
        return questions

    def rank_questions(self, questions: list[dict], company_name: str, role_title: str) -> list[dict]:
        deduped: dict[str, dict] = OrderedDict()
        for item in questions:
            key = item["text"].strip().lower()
            if key not in deduped:
                frequency = min(1.0, 0.5 + 0.1 * len(deduped))
                recency = 0.7
                relevance = 0.9 if role_title.lower() in item["text"].lower() else 0.8
                importance = float(item.get("importance", 0.75))
                item["frequency_score"] = frequency
                item["recency_score"] = recency
                item["relevance_score"] = relevance
                item["importance_score"] = importance
                item["final_score"] = compute_question_score(frequency, recency, relevance, importance)
                item["rationale"] = f"Ranked for {company_name} / {role_title} relevance."
                deduped[key] = item
        return sorted(deduped.values(), key=lambda item: item["final_score"], reverse=True)
