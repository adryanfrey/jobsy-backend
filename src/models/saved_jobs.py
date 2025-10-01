from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime, timezone


class SavedJobs(BaseModel):
    job_id: UUID
    user_id: UUID
    application_status: str  # TODO use literals
    notes: str
    applied_at: datetime
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
