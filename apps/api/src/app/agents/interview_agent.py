from __future__ import annotations

from app.providers.llm_provider import LLMProvider
from app.providers.voice_provider import STTProvider


class InterviewAgent:
    def __init__(self, llm: LLMProvider, stt: STTProvider) -> None:
        self.llm = llm
        self.stt = stt

    def starting_prompt(self) -> str:
        return "Tell me about yourself."

    def normalize_event_payload(self, event_type: str, payload: str | None) -> str:
        if event_type == "user_audio_chunk":
            return self.stt.transcribe(payload or "")
        return payload or ""

    def answer_clarification(self, question: str) -> str:
        return self.llm.answer_clarification(question)
