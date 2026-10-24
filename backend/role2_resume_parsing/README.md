# Role 2: Resume Parsing & Candidate Profiler

**Assigned Member:** Member 2  
**Scope:** Parse uploaded resumes (PDF / DOCX) into standardized candidate skill profiles adhering to `data/contracts/shared_data_contract.json#definitions/CandidateProfile`.

---

## 🛠️ Responsibilities & Tasks
1. Extract candidate identity, education, and total experience.
2. Structure technical capabilities into the 12 RADIX categories with realistic proficiency levels (1-10) and supporting evidence quotes.
3. Extract candidate workplace parameters (Parameters 164-166) based on past projects and role descriptions.
4. Integrate with LLM (OpenAI / Gemini / Anthropic) in `parser.py`.

---

## 🧪 Testing Locally
```bash
curl -X POST http://localhost:8000/api/v1/resume/parse \
  -F "raw_text=Senior Software Engineer with 6 years experience in Distributed Systems, GCP, and Kubernetes"
```
