from __future__ import annotations

from sqlalchemy import Float, JSON, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.mixins import TimestampMixin


class JobTarget(TimestampMixin, Base):
    __tablename__ = "job_targets"

    id: Mapped[int] = mapped_column(primary_key=True)
    job_posting_url: Mapped[str] = mapped_column(String(2048), unique=True, index=True)
    company_name: Mapped[str | None] = mapped_column(String(255), nullable=True)
    role_title: Mapped[str | None] = mapped_column(String(255), nullable=True)
    job_description: Mapped[str | None] = mapped_column(Text, nullable=True)
    extraction_confidence: Mapped[float | None] = mapped_column(Float, nullable=True)
    raw_tinyfish_result: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    raw_page_text: Mapped[str | None] = mapped_column(Text, nullable=True)
    status: Mapped[str] = mapped_column(String(50), default="created")

    sources = relationship("Source", back_populates="job_target", cascade="all, delete-orphan")
    questions = relationship("Question", back_populates="job_target", cascade="all, delete-orphan")
    sessions = relationship("InterviewSession", back_populates="job_target", cascade="all, delete-orphan")
