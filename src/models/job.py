from pydantic import BaseModel, Field
from datetime import datetime, timezone
from uuid import UUID, uuid4
from typing import List


class Job(BaseModel):
    job_id: UUID = Field(default_factory=uuid4)
    title: str
    company: str
    location: str
    source_url: str
    description: str
    technologies_and_tools: List[str]  # TODO use literals
    workplace_type: List[str]  # TODO use literals
    posted_at: datetime
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
