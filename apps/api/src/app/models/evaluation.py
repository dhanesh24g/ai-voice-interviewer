from __future__ import annotations

from datetime import datetime

from sqlalchemy import DateTime, Float, ForeignKey, JSON, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Evaluation(Base):
    __tablename__ = "evaluations"

    id: Mapped[int] = mapped_column(primary_key=True)
    session_id: Mapped[int] = mapped_column(ForeignKey("interview_sessions.id"), index=True)
    turn_id: Mapped[int | None] = mapped_column(ForeignKey("interview_turns.id"), nullable=True)
    score: Mapped[float] = mapped_column(Float)
    strengths: Mapped[list[str]] = mapped_column(JSON)
    weaknesses: Mapped[list[str]] = mapped_column(JSON)
    missing_points: Mapped[list[str]] = mapped_column(JSON)
    suggestion: Mapped[str | None] = mapped_column(Text, nullable=True)
    raw_payload: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))

    session = relationship("InterviewSession", back_populates="evaluations")


class FeedbackReport(Base):
    __tablename__ = "feedback_reports"

    id: Mapped[int] = mapped_column(primary_key=True)
    session_id: Mapped[int] = mapped_column(ForeignKey("interview_sessions.id"), index=True, unique=True)
    summary: Mapped[str] = mapped_column(Text)
    overall_score: Mapped[float] = mapped_column(Float)
    role_alignment: Mapped[float] = mapped_column(Float, default=0.0)
    answer_quality: Mapped[float] = mapped_column(Float, default=0.0)
    improvement_momentum: Mapped[float] = mapped_column(Float, default=0.0)
    strengths: Mapped[list[str]] = mapped_column(JSON)
    improvement_areas: Mapped[list[str]] = mapped_column(JSON)
    prep_guidance: Mapped[list[str]] = mapped_column(JSON)
    raw_payload: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))

    session = relationship("InterviewSession", back_populates="feedback_report")


class EvaluationRun(Base):
    __tablename__ = "evaluation_runs"

    id: Mapped[int] = mapped_column(primary_key=True)
    job_target_id: Mapped[int | None] = mapped_column(ForeignKey("job_targets.id"), nullable=True)
    session_id: Mapped[int | None] = mapped_column(ForeignKey("interview_sessions.id"), nullable=True)
    run_type: Mapped[str] = mapped_column(String(100))
    status: Mapped[str] = mapped_column(String(50), default="queued")
    metrics: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
