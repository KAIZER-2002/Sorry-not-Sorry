from datetime import datetime

from pydantic import BaseModel, Field


class ExcuseRequest(BaseModel):
    category: str = Field(..., min_length=1, max_length=100)
    audience: str = Field(..., min_length=1, max_length=100)
    tone: str = Field(..., min_length=1, max_length=50)
    length: str = Field(..., min_length=1, max_length=50)


class ExcuseItem(BaseModel):
    text: str
    believability: int
    drama: int
    risk: int


class ExcuseResponse(BaseModel):
    excuses: list[ExcuseItem]


class ExcuseHistoryItem(ExcuseResponse):
    id: int
    category: str
    audience: str
    tone: str
    length: str
    created_at: datetime

    class Config:
        from_attributes = True
