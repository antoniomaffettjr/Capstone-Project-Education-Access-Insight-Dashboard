# src/backend/routers/data.py

from typing import List

from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session

from .. import models, schemas
from ..database import get_db, Base, engine

# Create tables on first run (simple for now)
Base.metadata.create_all(bind=engine)

router = APIRouter()


@router.post("/upload", summary="Upload dataset (CSV placeholder)")
async def upload_data(file: UploadFile = File(...)):
    """
    Placeholder endpoint for CSV upload.
    Later: parse CSV, store in Google Cloud Storage, load into SQLite.
    """
    # For now, just confirm we got the file.
    return {
        "filename": file.filename,
        "message": "Upload endpoint hit successfully (implementation coming soon).",
    }


@router.get(
    "/retrieve",
    response_model=List[schemas.EducationMetric],
    summary="Retrieve education metrics (simple demo)",
)
def retrieve_data(
    country_iso: str | None = None,
    db: Session = Depends(get_db),
):
    """
    Basic data retrieval.
    Right now this just returns whatever is in the DB.
    Later, you'll filter by country, year, etc.
    """
    query = db.query(models.EducationMetric, models.Country).join(models.Country)

    if country_iso:
        query = query.filter(models.Country.iso_code == country_iso.upper())

    results = query.all()

    # Map to schema manually
    response: List[schemas.EducationMetric] = []
    for metric, country in results:
        response.append(
            schemas.EducationMetric(
                id=metric.id,
                year=metric.year,
                literacy_rate=metric.literacy_rate,
                primary_enrollment=metric.primary_enrollment,
                secondary_enrollment=metric.secondary_enrollment,
                gender_gap_enrollment=metric.gender_gap_enrollment,
                country_name=country.name,
            )
        )

    return response


@router.get(
    "/insights/summary",
    response_model=schemas.InsightSummary,
    summary="Basic insight summary",
)
def get_insight_summary(db: Session = Depends(get_db)):
    """
    Very simple stub for insights.
    Later: compute real stats (avg literacy, biggest improvements, etc.).
    """
    total_countries = db.query(models.Country).count()
    if total_countries == 0:
        example = "No data loaded yet. Upload a dataset to see insights."
        year_range = "N/A"
    else:
        # You can improve this later
        example = "Example: Once data is loaded, we will show trends here."
        year_range = "TBD"

    return schemas.InsightSummary(
        total_countries=total_countries,
        year_range=year_range,
        example_insight=example,
    )
