# 🔥 Trail Guardian Pro

**Next-generation wildfire-aware trail intelligence platform** — Real-time threat scoring, community intelligence, and firefighter tools to keep outdoor enthusiasts safe during fire season.

## The Problem

Every fire season, outdoor enthusiasts face a critical information gap: **They don't know if the trails they love are safe.** OnX Maps helps them navigate terrain, but it doesn't tell them about active fires, smoke impacts, or evacuation zones. This puts hikers, bikers, and runners at risk.

## The Solution

**Trail Guardian Pro** combines real-time fire data, intelligent threat scoring, and community intelligence into a single platform that answers one critical question: **Is this trail safe right now?**

## Current Features (MVP - Phase 1A)

✅ **Interactive Trail Map**
- Visual map of all trails with threat level indicators
- Color-coded markers (Green: Safe, Orange: Caution, Red: High Risk)
- Click-to-view detailed trail information
- Zoom and pan to explore regions

✅ **Trail Database**
- Trail name, description, difficulty, and distance
- Threat score calculation (0-100 scale)
- Active fire counts near trails
- Distance to nearest fire reports
- Persistent storage with PostgreSQL

✅ **RESTful API**
- `/api/v1/trails/` - List all trails
- `/api/v1/trails/{id}` - Get specific trail details
- Create new trails
- Full Swagger documentation at `/docs`

✅ **Full-Stack Architecture**
- **Backend**: FastAPI (Python) with async database support
- **Frontend**: React with Leaflet mapping
- **Database**: PostgreSQL with PostGIS for geospatial data
- **Cache**: Redis for performance optimization
- **Infrastructure**: Docker + Docker Compose for easy deployment

---

## 🗺️ Product Vision

### What Makes Trail Guardian Different

1. **Real-Time Threat Intelligence** - Not just "there's a fire nearby," but a calculated risk score based on multiple factors
2. **Community-Driven Safety** - Users report trail conditions, closures, and hazards in real-time
3. **Firefighter Integration** - Emergency responders get access to evacuation zones and trail network data
4. **Integration Ready** - Works alongside OnX Maps for complete outdoor safety solution

### The Threat Score Algorithm

Each trail gets a score (0-100) based on:
- Distance to active fires
- Number of fires in region
- Fire intensity and spread direction
- Weather conditions (wind, humidity, temperature)
- Historical fire patterns
- Recent trail closure reports
- Air quality (AQI)

**Example:**
- Trail 5km from small fire + light smoke = **45/100 (Caution)**
- Trail 15km from major fire + evacuation zone nearby = **78/100 (High Risk)**
- Trail 50km+ from any fires + clear conditions = **15/100 (Safe)**

---

## 📋 Roadmap: Next 4 Weeks

### Week 1: Real Fire Data Integration
- [ ] Connect to NASA FIRMS API for live fire data
- [ ] Parse and store active fire coordinates
- [ ] Automatically update threat scores based on real fires
- [ ] Add fire clusters and intensity visualization on map

### Week 2: Advanced Threat Scoring
- [ ] Implement multi-factor threat calculation algorithm
- [ ] Add weather API integration (wind, humidity, temperature)
- [ ] Include historical fire pattern analysis
- [ ] Create threat score breakdown/transparency view
- [ ] Real-time alerts when fires move near trails

### Week 3: Community Intelligence
- [ ] User authentication system (signup/login)
- [ ] Trail condition reporting (open/closed/hazardous)
- [ ] Photo uploads for trail conditions
- [ ] Community ratings and reviews
- [ ] Comment system for user discussions
- [ ] Report flags for dangerous/misinformation

### Week 4: Firefighter Tools & Polish
- [ ] Firefighter dashboard with emergency access
- [ ] Evacuation zone mapping
- [ ] Trail network analysis for fire response planning
- [ ] Email/SMS notifications for critical alerts
- [ ] Mobile optimization
- [ ] Performance optimization and bug fixes

---

## 🚀 Quick Start

### Prerequisites
- Docker & Docker Compose
- Node.js 16+ (for frontend development)
- Git

### Local Development

**1. Clone and setup:**
```bash
git clone https://github.com/JRodAmazing/onx-trail-guardian.git
cd onx-trail-guardian
```

**2. Start the full stack:**
```bash
docker-compose up
```

This starts:
- PostgreSQL database on `localhost:5432`
- Redis cache on `localhost:6379`
- FastAPI backend on `localhost:8000`

**3. Start the frontend (in another terminal):**
```bash
cd frontend
npm install
npm start
```

Frontend opens at `http://localhost:3000`

**4. Access the API:**
- Swagger Docs: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### Add Sample Trails

Go to http://localhost:8000/docs and use the POST `/api/v1/trails/` endpoint:

```json
{
  "name": "Pine Ridge Trail",
  "description": "Popular hiking trail with scenic views",
  "latitude": 40.7128,
  "longitude": -74.0060,
  "difficulty": "moderate",
  "length_miles": 5.2,
  "threat_score": 45,
  "last_fire_report_distance_km": 25.5,
  "active_fires_nearby": 2
}
```

---

## 📁 Project Structure

```
trail-guardian-pro/
├── backend/                 # FastAPI application
│   ├── app/
│   │   ├── main.py         # App entry point
│   │   ├── models/         # Database models
│   │   ├── api/v1/         # API endpoints
│   │   ├── core/           # Config, database, security
│   │   └── services/       # Business logic
│   ├── requirements.txt    # Python dependencies
│   ├── Dockerfile          # Container config
│   └── .env               # Environment variables
│
├── frontend/               # React application
│   ├── src/
│   │   ├── components/    # React components
│   │   ├── App.js        # Main app component
│   │   └── App.css       # Styling
│   ├── package.json      # Node dependencies
│   └── public/           # Static files
│
├── docker-compose.yml      # Multi-container orchestration
└── README.md              # This file
```

---

## 🛠️ Tech Stack

**Backend:**
- FastAPI - Modern, fast web framework
- SQLAlchemy - ORM for database
- AsyncPG - Async PostgreSQL driver
- Pydantic - Data validation
- PostGIS - Geospatial queries

**Frontend:**
- React 18 - UI framework
- Leaflet - Interactive mapping
- Axios - HTTP client

**Infrastructure:**
- PostgreSQL 15 + PostGIS - Spatial database
- Redis 7 - Caching and task queue
- Docker - Containerization

---

## 🔑 Environment Variables

Create a `.env` file in the `backend/` folder:

```env
# Application
APP_NAME=Trail Guardian Pro
DEBUG=True
ENVIRONMENT=development
SECRET_KEY=your-secret-key-here

# Database
DATABASE_URL=postgresql://postgres:postgres@postgres:5432/trailguardian

# Redis
REDIS_URL=redis://redis:6379/0
CELERY_BROKER_URL=redis://redis:6379/1

# APIs (get free keys)
FIRMS_API_KEY=your_nasa_firms_key
MAPBOX_ACCESS_TOKEN=your_mapbox_token
OPENAI_API_KEY=your_openai_key (optional)

# AWS S3 (optional)
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_S3_BUCKET=trailguardian-photos

# CORS
CORS_ORIGINS=["http://localhost:3000","http://localhost:8000"]
```

---

## 📊 API Endpoints (Current)

### Trails
- `GET /api/v1/trails/` - List all trails
- `POST /api/v1/trails/` - Create a new trail
- `GET /api/v1/trails/{trail_id}` - Get specific trail

### System
- `GET /` - API root info
- `GET /health` - Health check
- `GET /docs` - Swagger documentation

---

## 🤝 Contributing

Want to help? We're looking for:
- Full-stack developers
- GIS/mapping specialists
- Fire data scientists
- UI/UX designers

---

## 📝 License

MIT License - See LICENSE file for details

---

## 📞 Contact

**Project Lead:** JRodAmazing  
**GitHub:** https://github.com/JRodAmazing/onx-trail-guardian

---

## 🔥 Current Status

**Phase 1A (MVP):** ✅ Complete
- [x] Backend API framework
- [x] Database and models
- [x] Interactive map with trails
- [x] Basic threat scoring
- [x] Docker deployment

**Phase 1B (In Progress):** 🚧
- [ ] Real NASA FIRMS fire data
- [ ] Advanced threat algorithm
- [ ] Weather integration
- [ ] User authentication

**Phase 2 (Coming Soon):** 📋
- [ ] Community reporting
- [ ] Firefighter tools
- [ ] Mobile app
- [ ] Production deployment

---

**Built with ❤️ for outdoor safety. Made with 🔥 from coffee.**
