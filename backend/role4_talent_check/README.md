# Role 4: Talent Check Benchmarking Engine

**Assigned Member:** Member 4  
**Scope:** Compare candidate profiles against standardized company bars (e.g. Google, Microsoft, Oracle) across the 12 RADIX categories + workplace parameters (164-166).

---

## 🛠️ Responsibilities & Tasks
1. Leverage company skillsets from `data/mocks/talent_check_company_skillsets.json`.
2. Compute category deltas: $\text{delta} = \text{Candidate Level} - \text{Company Bar Level}$.
3. Calculate fit percentage and status (`Meets Bar`, `Potential Fit`, `Below Bar`).
4. Output schema complying with `data/contracts/shared_data_contract.json#definitions/TalentCheckResult`.

---

## 🧪 Testing Locally
```bash
# 1. Fetch available benchmark companies
curl http://localhost:8000/api/v1/talent-check/companies

# 2. Evaluate fit against Google
curl -X POST http://localhost:8000/api/v1/talent-check/evaluate \
  -H "Content-Type: application/json" \
  -d '{"company_id": "google"}'
```
