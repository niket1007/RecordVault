from pydantic import BaseModel, Field
from datetime import datetime

class UserRegRecords(BaseModel):
    email_id: str
    password: str
    created_at: datetime = Field(default_factory=lambda: datetime.now())