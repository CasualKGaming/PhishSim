from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from enum import Enum
from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=256)


class UserLogin(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    role: str
    created_at: datetime
    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class TemplateCreate(BaseModel):
    name: str
    subject: str
    body_html: str

class TemplateOut(TemplateCreate):
    id: int
    created_at: datetime
    class Config:
        from_attributes = True

class CampaignStatus(str, Enum):
    draft = "draft"
    scheduled = "scheduled"
    completed = "completed"

class CampaignCreate(BaseModel):
    name: str
    template_id: int

class CampaignOut(CampaignCreate):
    id: int
    status: CampaignStatus
    created_at: datetime
    class Config:
        from_attributes = True
