from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.deps import get_db
from app.schemas.question import QuestionResponse
from app.services.repositories import QuestionRepository

router = APIRouter()


@router.get("/{job_target_id}", response_model=list[QuestionResponse])
def get_question_bank(job_target_id: int, db: Session = Depends(get_db)):
    return QuestionRepository(db).list_by_job_target(job_target_id)
