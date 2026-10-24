"""
Role 5: Skill Matcher & Gap Analysis Engine
Compares CandidateProfile against JDSkillExtraction to output:
- Match percentage
- Strong matches
- Gaps (with HIGH, MEDIUM, LOW severity & actionable learning recommendations)
"""

from typing import Dict, Any, List

class SkillMatcher:
    def match(self, candidate_profile: Dict[str, Any], jd_skills: Dict[str, Any]) -> Dict[str, Any]:
        cand_skills = candidate_profile.get("skills_profile", [])
        cand_map = {s.get("category"): s for s in cand_skills}

        jd_required = jd_skills.get("skills_required", [])
        strong_matches = []
        gaps = []
        total_weight = 0
        earned_weight = 0

        for req in jd_required:
            category = req.get("category")
            req_skill_name = req.get("skill_name")
            req_level = req.get("required_level", 7)
            is_mandatory = req.get("is_mandatory", True)
            weight = 2 if is_mandatory else 1
            total_weight += weight

            cand_entry = cand_map.get(category)
            cand_level = cand_entry.get("level", 0) if cand_entry else 0

            if cand_level >= req_level:
                earned_weight += weight
                strong_matches.append({
                    "category": category,
                    "jd_skill": req_skill_name,
                    "candidate_skill": cand_entry.get("skill_name", req_skill_name) if cand_entry else req_skill_name,
                    "candidate_level": cand_level,
                    "required_level": req_level,
                    "score": round((cand_level / max(req_level, 1)) * 100, 1)
                })
            else:
                level_gap = req_level - cand_level
                earned_weight += weight * max(0, (cand_level / max(req_level, 1)))

                if is_mandatory and level_gap >= 2:
                    severity = "HIGH"
                elif level_gap >= 2 or is_mandatory:
                    severity = "MEDIUM"
                else:
                    severity = "LOW"

                gaps.append({
                    "category": category,
                    "missing_or_deficient_skill": req_skill_name,
                    "required_level": req_level,
                    "candidate_level": cand_level,
                    "severity": severity,
                    "recommendation": f"Complete advanced project/course in {category} focused on {req_skill_name} to bridge the {level_gap}-point gap."
                })

        match_pct = round((earned_weight / max(total_weight, 1)) * 100, 1)

        return {
            "candidate_id": candidate_profile.get("candidate_id", "CAND-001"),
            "job_id": jd_skills.get("job_id", "JD-001"),
            "match_percentage": match_pct,
            "strong_matches_count": len(strong_matches),
            "gaps_count": len(gaps),
            "strong_matches": strong_matches,
            "gaps": gaps
        }
