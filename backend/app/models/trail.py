"""Trail data model."""
from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from app.core.database import Base

class Trail(Base):
    __tablename__ = "trails"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    description = Column(String(1000))
    latitude = Column(Float)
    longitude = Column(Float)
    difficulty = Column(String(50))
    length_miles = Column(Float)
    threat_score = Column(Integer, default=0)
    last_fire_report_distance_km = Column(Float)
    active_fires_nearby = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
