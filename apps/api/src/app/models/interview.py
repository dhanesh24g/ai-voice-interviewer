from __future__ import annotations

from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.mixins import TimestampMixin


class InterviewSession(TimestampMixin, Base):
    __tablename__ = "interview_sessions"

    id: Mapped[int] = mapped_column(primary_key=True)
    job_target_id: Mapped[int] = mapped_column(ForeignKey("job_targets.id"), index=True)
    status: Mapped[str] = mapped_column(String(50), default="started")
    mode: Mapped[str] = mapped_column(String(50), default="text")
    current_question_index: Mapped[int] = mapped_column(default=0)
    stop_reason: Mapped[str | None] = mapped_column(String(255), nullable=True)
    started_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    ended_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    job_target = relationship("JobTarget", back_populates="sessions")
    turns = relationship("InterviewTurn", back_populates="session", cascade="all, delete-orphan")
    evaluations = relationship("Evaluation", back_populates="session", cascade="all, delete-orphan")
    feedback_report = relationship("FeedbackReport", back_populates="session", uselist=False)


class InterviewTurn(Base):
    __tablename__ = "interview_turns"

    id: Mapped[int] = mapped_column(primary_key=True)
    session_id: Mapped[int] = mapped_column(ForeignKey("interview_sessions.id"), index=True)
    question_id: Mapped[int | None] = mapped_column(ForeignKey("questions.id"), nullable=True)
    turn_index: Mapped[int]
    agent_prompt: Mapped[str] = mapped_column(Text)
    user_response: Mapped[str | None] = mapped_column(Text, nullable=True)
    event_type: Mapped[str] = mapped_column(String(50), default="user_text")
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))

    session = relationship("InterviewSession", back_populates="turns")
