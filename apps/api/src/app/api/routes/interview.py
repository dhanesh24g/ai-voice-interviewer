import logging

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.deps import get_db, get_services

logger = logging.getLogger(__name__)
from app.schemas.evaluation import FeedbackReportResponse
from app.schemas.interview import InterviewSessionEventRequest, InterviewSessionResponse, InterviewSessionStartRequest
from app.services.container import ServiceContainer
from app.services.repositories import JobTargetRepository

router = APIRouter()


@router.post("/session/start", response_model=InterviewSessionResponse)
def start_session(
    payload: InterviewSessionStartRequest,
    db: Session = Depends(get_db),
    services: ServiceContainer = Depends(get_services),
):
    job_target = JobTargetRepository(db).get(payload.job_target_id)
    if not job_target:
        raise HTTPException(status_code=404, detail="Job target not found")
    interview_service = services.with_db(db)["interview_service"]
    return interview_service.start_session(job_target, payload.mode)


@router.post("/session/{session_id}/event", response_model=InterviewSessionResponse)
def post_session_event(
    session_id: int,
    payload: InterviewSessionEventRequest,
    db: Session = Depends(get_db),
    services: ServiceContainer = Depends(get_services),
):
    svc = services.with_db(db)["interview_service"]
    session = svc.repo.get_session(session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Interview session not found")
    job_target = JobTargetRepository(db).get(session.job_target_id)
    if not job_target:
        raise HTTPException(status_code=404, detail="Job target not found")
    try:
        return svc.handle_event(session, job_target, payload.event_type, payload.payload)
    except Exception as exc:
        logger.exception(f"[EVENT_ERROR] session={session_id} event={payload.event_type} | {type(exc).__name__}: {exc}")
        raise HTTPException(status_code=500, detail=f"Failed to process event: {type(exc).__name__}")


@router.post("/session/{session_id}/stop", response_model=InterviewSessionResponse)
def stop_session(
    session_id: int,
    db: Session = Depends(get_db),
    services: ServiceContainer = Depends(get_services),
):
    svc = services.with_db(db)["interview_service"]
    session = svc.repo.get_session(session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Interview session not found")
    return svc.stop_session(session, "manual_stop")


@router.get("/session/{session_id}/feedback", response_model=FeedbackReportResponse)
def get_feedback(
    session_id: int,
    db: Session = Depends(get_db),
    services: ServiceContainer = Depends(get_services),
):
    svc = services.with_db(db)["interview_service"]
    evaluation_service = services.with_db(db)["evaluation_service"]
    session = svc.repo.get_session(session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Interview session not found")
    return evaluation_service.generate_feedback(session)
