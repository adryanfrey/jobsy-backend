from typing import List
from uuid import UUID
from pydantic import BaseModel, Field
from datetime import datetime, timezone


class UserPreferences(BaseModel):
    user_id: UUID
    locations: List[str]
    workplace_types: List[str]  # TODO use literals
    technologies_and_tools: List[str]  # TODO use literals
    seniority_levels: List[str]  # TODO use literals
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
