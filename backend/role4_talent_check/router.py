"""
FastAPI Router for Role 4: Talent Check
Endpoints:
- GET  /api/v1/talent-check/companies (list benchmark companies)
- POST /api/v1/talent-check/evaluate  (evaluate candidate profile vs company bar)
"""

from fastapi import APIRouter, HTTPException, Body
from typing import Dict, Any
from .scorer import TalentCheckScorer

router = APIRouter(prefix="/api/v1/talent-check", tags=["Role 4 - Talent Check Benchmarking"])
scorer = TalentCheckScorer()

@router.get("/companies")
async def get_companies():
    return scorer.get_available_companies()

@router.post("/evaluate")
async def evaluate_fit(
    payload: Dict[str, Any] = Body(...)
):
    try:
        candidate_profile = payload.get("candidate_profile")
        company_id = payload.get("company_id", "google")
        
        if not candidate_profile:
            # Fallback to local mock candidate profile for seamless testing
            import json
            from pathlib import Path
            mock_path = Path(__file__).resolve().parent.parent.parent / "data" / "mocks" / "mock_candidate_profile.json"
            if mock_path.exists():
                with open(mock_path, "r", encoding="utf-8") as f:
                    candidate_profile = json.load(f)
            else:
                raise HTTPException(status_code=400, detail="Missing candidate_profile in request body.")

        return scorer.evaluate_candidate(candidate_profile, company_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
