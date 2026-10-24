# Role 5: Skill Matching & Gap Analysis Engine

**Assigned Member:** Member 5  
**Scope:** Compare extracted JD requirements (Role 1) against Candidate Skill Profile (Role 2) to calculate match percentages and pinpoint prioritized learning gaps.

---

## 🛠️ Responsibilities & Tasks
1. Consume `CandidateProfile` and `JDSkillExtraction` defined in `data/contracts/shared_data_contract.json`.
2. Compute weighted match percentages factoring mandatory vs nice-to-have requirements.
3. Categorize gaps into `HIGH`, `MEDIUM`, and `LOW` severity.
4. Generate actionable upskilling recommendations for each deficient category.
5. Enhance fuzzy string matching / semantic embedding similarity in `matcher.py`.

---

## 🧪 Testing Locally
```bash
# Test with default mock payloads
curl -X POST http://localhost:8000/api/v1/skills/match \
  -H "Content-Type: application/json" \
  -d '{}'
```
