"""
Role 4: Talent Check Benchmark Scorer
Compares a CandidateProfile against Company Benchmark Skillsets across the 12 RADIX categories
and calculates fit scores and workplace parameter alignment.
"""

import json
from pathlib import Path
from typing import Dict, Any, List

class TalentCheckScorer:
    def __init__(self, data_path: str = None):
        if not data_path:
            self.data_path = Path(__file__).resolve().parent.parent.parent / "data" / "mocks" / "talent_check_company_skillsets.json"
        else:
            self.data_path = Path(data_path)
        self.companies = self._load_companies()

    def _load_companies(self) -> Dict[str, Any]:
        if self.data_path.exists():
            with open(self.data_path, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    def get_available_companies(self) -> List[Dict[str, str]]:
        """Returns list of company IDs and names available in benchmarks."""
        results = []
        for cid, data in self.companies.items():
            results.append({
                "company_id": cid,
                "company_name": data.get("company_name", cid.capitalize())
            })
        return results

    def evaluate_candidate(self, candidate_profile: Dict[str, Any], company_id: str) -> Dict[str, Any]:
        """
        Evaluates candidate against target company hiring bar.
        """
        company_data = self.companies.get(company_id.lower())
        if not company_data:
            # Fallback to first company or empty
            first_key = next(iter(self.companies), None)
            if first_key:
                company_data = self.companies[first_key]
                company_id = first_key
            else:
                return {"error": f"Company '{company_id}' not found in benchmark datasets."}

        company_skills = company_data.get("skills_benchmark", {})
        cand_skills_map = {
            s.get("category"): s.get("level", 5)
            for s in candidate_profile.get("skills_profile", [])
        }

        evaluations = []
        total_delta = 0
        passed_count = 0
        total_categories = len(company_skills) or 12

        for category, bar_level in company_skills.items():
            cand_level = cand_skills_map.get(category, 5)
            delta = cand_level - bar_level
            passed = delta >= 0
            if passed:
                passed_count += 1
            total_delta += delta

            evaluations.append({
                "category": category,
                "candidate_level": cand_level,
                "company_bar_level": bar_level,
                "delta": delta,
                "passed": passed
            })

        # Calculate normalized score (0-100)
        fit_percentage = max(0, min(100, round((passed_count / total_categories) * 100, 1)))

        if fit_percentage >= 80:
            status = "Meets Bar"
        elif fit_percentage >= 60:
            status = "Potential Fit"
        else:
            status = "Below Bar"

        # Compare workplace parameters (164-166)
        cand_prefs = candidate_profile.get("workplace_preferences", {})
        comp_params = company_data.get("workplace_parameters", {})

        param_alignments = {
            "param_164_match": bool(cand_prefs.get("param_164_communication_style") and comp_params.get("param_164_communication_style")),
            "param_165_match": bool(cand_prefs.get("param_165_work_environment_pacing") and comp_params.get("param_165_work_environment_pacing")),
            "param_166_match": bool(cand_prefs.get("param_166_collaboration_breadth") and comp_params.get("param_166_collaboration_breadth"))
        }

        return {
            "candidate_id": candidate_profile.get("candidate_id", "CAND-001"),
            "company_id": company_id,
            "company_name": company_data.get("company_name", company_id),
            "overall_fit_score": fit_percentage,
            "status": status,
            "passed_categories": passed_count,
            "total_categories": total_categories,
            "skill_category_evaluations": evaluations,
            "parameter_alignments": param_alignments
        }
