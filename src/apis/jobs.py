from fastapi import APIRouter
from services.job import JobService

router = APIRouter()



@router.post("/search")
def search_jobs():
    return


@router.get("/")
def get_jobs():
    return