from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.deps import get_db, get_services
from app.schemas.evaluation import EvaluationRunRequest, EvaluationRunResponse
from app.services.container import ServiceContainer

router = APIRouter()


@router.post("/run", response_model=EvaluationRunResponse)
def run_evaluation(
    payload: EvaluationRunRequest,
    db: Session = Depends(get_db),
    services: ServiceContainer = Depends(get_services),
):
    svc = services.with_db(db)["evaluation_service"]
    return svc.run_system_evaluation(payload.job_target_id, payload.session_id, payload.run_type)
