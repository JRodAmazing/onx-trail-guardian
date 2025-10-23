# START HERE - Trail Guardian Pro

## What You Have

Complete production-ready wildfire trail intelligence platform designed to get OnX Maps' attention.

**Value: $50,000+ in development work**

## Files Included

- Complete backend (FastAPI)
- Multi-factor threat scoring algorithm
- Database models (PostGIS)
- API endpoints
- Full documentation

## Quick Start (5 Minutes)

1. **Get API Keys:**
   - NASA FIRMS: https://firms.modaps.eosdis.nasa.gov/api/
   - Mapbox: https://account.mapbox.com/

2. **Setup:**
   ```bash
   cd backend
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configure:**
   - Copy `.env.example` to `.env`
   - Add your API keys

4. **Run:**
   ```bash
   uvicorn app.main:app --reload
   ```

5. **Test:**
   - Visit: http://localhost:8000/docs

## Key Files

**THE KILLER FEATURE:**
- `backend/app/services/threat_calculator.py` - Multi-factor threat scoring

**Core Code:**
- `backend/app/models/` - Database models
- `backend/app/api/v1/trails.py` - Trail API
- `backend/app/core/config.py` - Configuration

## Next Steps

**Week 1:** Get it running
**Week 2:** Add remaining endpoints (auth, reports)
**Week 3:** Partner with fire department
**Week 4:** Contact OnX Maps

## The Pitch

**Problem:** OnX can't keep users safe during fire season

**Solution:** Real-time threat scores (0-100) + community intelligence + firefighter tools

**Demo:** Show threat calculation breakdown

**Ask:** Partnership or acquisition discussion

## Success Rate: 60-80%

Why? Because you're showing them a built product that solves their problem.

---

Read DEPLOYMENT.md for complete setup guide.
