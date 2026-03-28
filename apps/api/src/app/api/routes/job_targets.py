from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.deps import get_db, get_services
from app.schemas.job_target import JobTargetCreate, JobTargetExtractRequest, JobTargetResponse
from app.services.container import ServiceContainer

router = APIRouter()


@router.post("", response_model=JobTargetResponse, status_code=status.HTTP_201_CREATED)
def create_job_target(
    payload: JobTargetCreate,
    db: Session = Depends(get_db),
    services: ServiceContainer = Depends(get_services),
):
    job_service = services.with_db(db)["job_service"]
    return job_service.create_job_target(str(payload.job_posting_url))


@router.post("/extract", response_model=JobTargetResponse)
def extract_job_target(
    payload: JobTargetExtractRequest,
    db: Session = Depends(get_db),
    services: ServiceContainer = Depends(get_services),
):
    job_service = services.with_db(db)["job_service"]
    return job_service.extract_job_target(str(payload.job_posting_url))


@router.get("/{job_target_id}", response_model=JobTargetResponse)
def get_job_target(
    job_target_id: int,
    db: Session = Depends(get_db),
    services: ServiceContainer = Depends(get_services),
):
    job_service = services.with_db(db)["job_service"]
    item = job_service.get_job_target(job_target_id)
    if not item:
        raise HTTPException(status_code=404, detail="Job target not found")
    return item
