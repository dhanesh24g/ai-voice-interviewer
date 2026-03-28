from __future__ import annotations


class STTProvider:
    def transcribe(self, audio_payload: str) -> str:
        raise NotImplementedError


class TTSProvider:
    def synthesize(self, text: str) -> bytes:
        raise NotImplementedError


class MockSTTProvider(STTProvider):
    def transcribe(self, audio_payload: str) -> str:
        return audio_payload


class MockTTSProvider(TTSProvider):
    def synthesize(self, text: str) -> bytes:
        return text.encode("utf-8")
