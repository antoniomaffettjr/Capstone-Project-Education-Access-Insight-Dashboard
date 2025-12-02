# src/backend/schemas.py

from typing import Optional, List
from pydantic import BaseModel


class EducationMetricBase(BaseModel):
    year: int
    literacy_rate: Optional[float] = None
    primary_enrollment: Optional[float] = None
    secondary_enrollment: Optional[float] = None
    gender_gap_enrollment: Optional[float] = None


class EducationMetricCreate(EducationMetricBase):
    country_iso: str


class EducationMetric(EducationMetricBase):
    id: int
    country_name: str

    class Config:
        orm_mode = True


class InsightSummary(BaseModel):
    total_countries: int
    year_range: str
    example_insight: str
