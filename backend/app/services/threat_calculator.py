"""
Trail Threat Calculator - THE KILLER FEATURE

Multi-factor threat scoring algorithm that combines:
- Fire proximity (35%)
- Fire behavior (25%)
- Weather conditions (20%)
- Terrain exposure (15%)
- Historical risk (5%)
- Community reports (multiplier 1.0-1.5x)

Score: 0-100
- 0-30: LOW
- 31-60: MODERATE  
- 61-80: HIGH
- 81-100: EXTREME
"""

from typing import Dict
from datetime import datetime, timedelta
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.core.config import settings


class ThreatCalculator:
    """Calculate comprehensive threat scores for trails."""
    
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def calculate_trail_threat(self, trail_id: str) -> Dict:
        """
        Calculate threat score for a trail.
        
        Returns:
            {
                "threat_score": 73.5,
                "threat_level": "HIGH",
                "recommendation": "Avoid this trail",
                "breakdown": {...}
            }
        """
        # Get fire proximity score
        fire_proximity = await self._fire_proximity_score(trail_id)
        fire_behavior = await self._fire_behavior_score(trail_id)
        weather_risk = await self._weather_risk_score(trail_id)
        terrain_exposure = await self._terrain_exposure_score(trail_id)
        historical_risk = await self._historical_risk_score(trail_id)
        
        # Calculate weighted total
        base_score = (
            fire_proximity * settings.THREAT_WEIGHT_FIRE_PROXIMITY +
            fire_behavior * settings.THREAT_WEIGHT_FIRE_BEHAVIOR +
            weather_risk * settings.THREAT_WEIGHT_WEATHER +
            terrain_exposure * settings.THREAT_WEIGHT_TERRAIN +
            historical_risk * settings.THREAT_WEIGHT_HISTORICAL
        )
        
        # Apply community modifier
        community_mod = await self._community_modifier(trail_id)
        final_score = min(100, base_score * community_mod)
        
        return {
            "trail_id": trail_id,
            "threat_score": round(final_score, 2),
            "threat_level": self._get_level(final_score),
            "recommendation": self._get_recommendation(final_score),
            "breakdown": {
                "fire_proximity": round(fire_proximity, 2),
                "fire_behavior": round(fire_behavior, 2),
                "weather_risk": round(weather_risk, 2),
                "terrain_exposure": round(terrain_exposure, 2),
                "historical_risk": round(historical_risk, 2),
                "community_modifier": community_mod
            },
            "calculated_at": datetime.utcnow().isoformat()
        }
    
    async def _fire_proximity_score(self, trail_id: str) -> float:
        """
        Score based on distance to nearest fire.
        < 5km: 100
        5-15km: 70-100
        15-30km: 30-70
        > 30km: 0-30
        """
        # TODO: Query nearest active fire
        # For now, return sample score
        return 45.0
    
    async def _fire_behavior_score(self, trail_id: str) -> float:
        """
        Score based on fire intensity and fuel models.
        """
        # TODO: Check fuel models and fire perimeters
        return 35.0
    
    async def _weather_risk_score(self, trail_id: str) -> float:
        """
        Score based on weather conditions.
        Red flag warnings, wind, humidity.
        """
        # TODO: Query weather stations
        return 40.0
    
    async def _terrain_exposure_score(self, trail_id: str) -> float:
        """
        Score based on terrain characteristics.
        Slope, elevation, aspect.
        """
        # TODO: Analyze terrain
        return 30.0
    
    async def _historical_risk_score(self, trail_id: str) -> float:
        """
        Score based on historical fire activity.
        """
        return 30.0
    
    async def _community_modifier(self, trail_id: str) -> float:
        """
        Modifier based on recent community reports.
        Returns: 0.8 - 1.5
        """
        # TODO: Check recent trail reports
        return 1.0
    
    def _get_level(self, score: float) -> str:
        """Convert score to threat level."""
        if score >= 81:
            return "EXTREME"
        elif score >= 61:
            return "HIGH"
        elif score >= 31:
            return "MODERATE"
        else:
            return "LOW"
    
    def _get_recommendation(self, score: float) -> str:
        """Get human-readable recommendation."""
        if score >= 81:
            return "TRAIL CLOSURE RECOMMENDED - Extreme fire danger"
        elif score >= 61:
            return "HIGH RISK - Avoid this trail"
        elif score >= 31:
            return "MODERATE RISK - Exercise caution"
        else:
            return "LOW RISK - Trail appears safe"
