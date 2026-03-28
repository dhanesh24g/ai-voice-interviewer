from __future__ import annotations


def compute_question_score(
    frequency: float,
    recency: float,
    relevance: float,
    importance: float,
    weights: dict[str, float] | None = None,
) -> float:
    weights = weights or {
        "frequency": 0.3,
        "recency": 0.15,
        "relevance": 0.35,
        "importance": 0.2,
    }
    return round(
        frequency * weights["frequency"]
        + recency * weights["recency"]
        + relevance * weights["relevance"]
        + importance * weights["importance"],
        4,
    )
