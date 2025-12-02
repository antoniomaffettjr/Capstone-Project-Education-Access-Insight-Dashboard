# src/backend/models.py

from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base


class Country(Base):
    __tablename__ = "countries"

    id = Column(Integer, primary_key=True, index=True)
    iso_code = Column(String, unique=True, index=True)
    name = Column(String, index=True)

    metrics = relationship("EducationMetric", back_populates="country")


class EducationMetric(Base):
    __tablename__ = "education_metrics"

    id = Column(Integer, primary_key=True, index=True)
    country_id = Column(Integer, ForeignKey("countries.id"))
    year = Column(Integer, index=True)

    # Example indicators (you can adjust later)
    literacy_rate = Column(Float, nullable=True)
    primary_enrollment = Column(Float, nullable=True)
    secondary_enrollment = Column(Float, nullable=True)
    gender_gap_enrollment = Column(Float, nullable=True)

    country = relationship("Country", back_populates="metrics")
