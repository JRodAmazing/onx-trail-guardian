# Complete Deployment Guide

## Quick Start (5 Minutes)

### 1. Get API Keys (Required)

**NASA FIRMS** (Free):

- Go to: https://firms.modaps.eosdis.nasa.gov/api/
- Register for Map Key
- Copy your key

**Mapbox** (Free tier: 50k loads/month):

- Go to: https://account.mapbox.com/
- Create account
- Copy default public token

### 2. Setup Environment

```bash
# Navigate to project
cd trail-guardian-pro/backend

# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configure

```bash
# Copy example environment file
copy .env.example .env

# Edit .env and add:
# - Your NASA FIRMS key
# - Your Mapbox token
# - Your SECRET_KEY (generate with: openssl rand -hex 32)
```

### 4. Start Database (Docker)

```bash
# Start PostgreSQL with PostGIS
docker run -d \
  --name trailguardian-db \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=trailguardian \
  -p 5432:5432 \
  postgis/postgis:15-3.3

# Start Redis
docker run -d \
  --name trailguardian-redis \
  -p 6379:6379 \
  redis:7-alpine
```

### 5. Run API

```bash
# From backend directory with venv activated
uvicorn app.main:app --reload --port 8000
```

### 6. Test

Visit: http://localhost:8000/docs

---

## GitHub Deployment

### 1. Create Repository

```bash
# Initialize git
cd trail-guardian-pro
git init

# Create .gitignore
cat > .gitignore << EOF
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
ENV/

# Environment
.env
.env.local

# IDEs
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Database
*.db
*.sqlite3

# Logs
*.log
EOF

# Initial commit
git add .
git commit -m "Initial commit: Trail Guardian Pro"
```

### 2. Push to GitHub

```bash
# Create repo on GitHub first, then:
git remote add origin https://github.com/JRodAmazing/trail-guardian-pro.git
git branch -M main
git push -u origin main
```

### 3. Add README Badge

Add to top of README.md:

```markdown
![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109-green.svg)
![License](https://img.shields.io/badge/license-Proprietary-red.svg)
```

---

## Production Deployment

### Option 1: Railway (Easiest)

1. Go to: https://railway.app/
2. Connect GitHub repo
3. Add PostgreSQL + Redis services
4. Set environment variables
5. Deploy!

### Option 2: DigitalOcean

```bash
# Create Droplet (Ubuntu 22.04)
# SSH into server

# Install dependencies
sudo apt update
sudo apt install -y python3.11 python3.11-venv postgresql-15 redis-server

# Clone repo
git clone https://github.com/JRodAmazing/trail-guardian-pro.git
cd trail-guardian-pro/backend

# Setup
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Setup systemd service
sudo nano /etc/systemd/system/trailguardian.service
```

Add:

```ini
[Unit]
Description=Trail Guardian Pro API
After=network.target

[Service]
User=www-data
WorkingDirectory=/path/to/trail-guardian-pro/backend
Environment="PATH=/path/to/venv/bin"
ExecStart=/path/to/venv/bin/uvicorn app.main:app --host 0.0.0.0 --port 8000

[Install]
WantedBy=multi-user.target
```

```bash
# Start service
sudo systemctl enable trailguardian
sudo systemctl start trailguardian
```

### Option 3: Docker

Create `Dockerfile`:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc libpq-dev gdal-bin

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Create `docker-compose.yml`:

```yaml
version: "3.8"

services:
  api:
    build: ./backend
    ports:
      - "8000:8000"
    env_file:
      - ./backend/.env
    depends_on:
      - postgres
      - redis

  postgres:
    image: postgis/postgis:15-3.3
    environment:
      POSTGRES_DB: trailguardian
      POSTGRES_PASSWORD: postgres
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

volumes:
  postgres_data:
```

Run:

```bash
docker-compose up -d
```

---

## Environment Variables

All required environment variables:

```bash
# Required
SECRET_KEY=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
FIRMS_API_KEY=eyJ0eXAiOiJKV1QiLCJvcmlnaW4iOiJFYXJ0aGRhdGEgTG9naW4iLCJzaWciOiJlZGxqd3...
MAPBOX_ACCESS_TOKEN=pk.eyJ1IjoianJvZGFtYXppbmciLCJhIjoiY21oMnZ4YzEyMXVyOTJscG9yeWt6Z3NndyJ9...
DATABASE_URL=postgresql://user:jcroden25@gmail.com:5432/dbname

# Optional (for full features)
OPENAI_API_KEY=for_ml_features
AWS_ACCESS_KEY_ID=for_photo_uploads
AWS_SECRET_ACCESS_KEY=for_photo_uploads
SENDGRID_API_KEY=for_email_alerts
TWILIO_ACCOUNT_SID=for_sms_alerts
```

---

## Troubleshooting

**Problem:** `ModuleNotFoundError: No module named 'geoalchemy2'`
**Solution:** `pip install geoalchemy2`

**Problem:** Database connection refused
**Solution:** Check Docker containers running: `docker ps`

**Problem:** CORS errors
**Solution:** Add your frontend URL to `CORS_ORIGINS` in `.env`

---

## Performance Optimization

### Database Indexes

```sql
-- Add after initial setup
CREATE INDEX idx_trails_centroid ON trails USING GIST (centroid);
CREATE INDEX idx_active_fires_location ON active_fires USING GIST (location);
```

### Redis Caching

Set up caching in production:

- Fire data: 3 hour TTL
- Weather: 1 hour TTL
- Threat scores: 15 minute TTL

---

## Next Steps

1. ✅ Deploy to production
2. ✅ Test all endpoints
3. ✅ Monitor logs
4. ✅ Set up backups
5. ✅ Configure SSL/HTTPS
6. ✅ Add monitoring (Sentry)

---

## Support

- Documentation: README.md
- Issues: GitHub Issues
- Email: support@trailguardianpro.com
