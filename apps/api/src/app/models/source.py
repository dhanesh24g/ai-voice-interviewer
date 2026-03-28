from __future__ import annotations

from sqlalchemy import ForeignKey, JSON, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.mixins import TimestampMixin


class Source(TimestampMixin, Base):
    __tablename__ = "sources"

    id: Mapped[int] = mapped_column(primary_key=True)
    job_target_id: Mapped[int] = mapped_column(ForeignKey("job_targets.id"), index=True)
    source_url: Mapped[str] = mapped_column(String(2048))
    source_type: Mapped[str] = mapped_column(String(100))
    raw_tinyfish_result: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    parsed_text: Mapped[str | None] = mapped_column(Text, nullable=True)
    fetch_status: Mapped[str] = mapped_column(String(50), default="pending")

    job_target = relationship("JobTarget", back_populates="sources")
    questions = relationship("Question", back_populates="source")
