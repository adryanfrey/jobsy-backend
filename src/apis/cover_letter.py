from fastapi import APIRouter

router = APIRouter()


@router.post("/generate/job/{job_id}")
def generate_cover_letter(job_id: str):
    return
