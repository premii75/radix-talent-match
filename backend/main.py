"""
RADIX Talent Match - Unified Backend API Gateway
Hosts modular endpoints for all 5 Hackathon Roles:
- Role 1: /api/v1/jd
- Role 2: /api/v1/resume
- Role 4: /api/v1/talent-check
- Role 5: /api/v1/skills
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.role1_jd_analytics.router import router as jd_router
from backend.role2_resume_parsing.router import router as resume_router
from backend.role4_talent_check.router import router as talent_check_router
from backend.role5_skill_matching.router import router as skills_router

app = FastAPI(
    title="RADIX Talent Match Backend API",
    description="Unified API gateway powering the 5-role RADIX Talent Match system.",
    version="1.0.0"
)

# Enable CORS for local Lovable / React frontend (e.g. localhost:5173, localhost:3000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount modular routers
app.include_router(jd_router)
app.include_router(resume_router)
app.include_router(talent_check_router)
app.include_router(skills_router)

@app.get("/")
def root():
    return {
        "status": "online",
        "service": "RADIX Talent Match API Gateway",
        "docs_url": "/docs",
        "modules": {
            "role1_jd_analytics": "/api/v1/jd/extract",
            "role2_resume_parsing": "/api/v1/resume/parse",
            "role4_talent_check": "/api/v1/talent-check/evaluate",
            "role5_skill_matching": "/api/v1/skills/match"
        }
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}
