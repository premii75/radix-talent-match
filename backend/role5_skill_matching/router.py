"""
FastAPI Router for Role 5: Skill Matching & Gap Analysis
Endpoints:
- POST /api/v1/skills/match (takes candidate_profile and jd_skills or uses mocks)
"""

from fastapi import APIRouter, HTTPException, Body
from typing import Dict, Any
import json
from pathlib import Path
from .matcher import SkillMatcher

router = APIRouter(prefix="/api/v1/skills", tags=["Role 5 - Skill Matching & Gap Analysis"])
matcher = SkillMatcher()

@router.post("/match")
async def match_skills(payload: Dict[str, Any] = Body(...)):
    try:
        candidate_profile = payload.get("candidate_profile")
        jd_skills = payload.get("jd_skills")

        mocks_dir = Path(__file__).resolve().parent.parent.parent / "data" / "mocks"

        # Load fallback mock data if omitted for easy frontend testing
        if not candidate_profile:
            cand_path = mocks_dir / "mock_candidate_profile.json"
            if cand_path.exists():
                with open(cand_path, "r", encoding="utf-8") as f:
                    candidate_profile = json.load(f)
            else:
                raise HTTPException(status_code=400, detail="Missing candidate_profile")

        if not jd_skills:
            jd_path = mocks_dir / "mock_jd_skills.json"
            if jd_path.exists():
                with open(jd_path, "r", encoding="utf-8") as f:
                    jd_skills = json.load(f)
            else:
                raise HTTPException(status_code=400, detail="Missing jd_skills")

        return matcher.match(candidate_profile, jd_skills)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
