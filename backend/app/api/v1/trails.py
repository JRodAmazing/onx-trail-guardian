"""Trail endpoints."""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.trail import Trail
from app.core.database import get_db
from pydantic import BaseModel

router = APIRouter(prefix="/api/v1/trails", tags=["trails"])

class TrailCreate(BaseModel):
    name: str
    description: str
    latitude: float
    longitude: float
    difficulty: str
    length_miles: float
    threat_score: int
    last_fire_report_distance_km: float
    active_fires_nearby: int

class TrailResponse(BaseModel):
    id: int
    name: str
    description: str
    latitude: float
    longitude: float
    difficulty: str
    length_miles: float
    threat_score: int
    last_fire_report_distance_km: float
    active_fires_nearby: int

    class Config:
        from_attributes = True

@router.get("/", response_model=list[TrailResponse])
async def get_trails(db: AsyncSession = Depends(get_db)):
    """Get all trails."""
    result = await db.execute(select(Trail))
    trails = result.scalars().all()
    return trails

@router.post("/", response_model=TrailResponse)
async def create_trail(trail: TrailCreate, db: AsyncSession = Depends(get_db)):
    """Create a new trail."""
    new_trail = Trail(**trail.dict())
    db.add(new_trail)
    await db.commit()
    await db.refresh(new_trail)
    return new_trail

@router.get("/{trail_id}", response_model=TrailResponse)
async def get_trail(trail_id: int, db: AsyncSession = Depends(get_db)):
    """Get a specific trail."""
    result = await db.execute(select(Trail).where(Trail.id == trail_id))
    trail = result.scalar_one_or_none()
    if not trail:
        raise HTTPException(status_code=404, detail="Trail not found")
    return trail
