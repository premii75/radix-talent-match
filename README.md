# RADIX Talent Match Platform 🚀

An AI-native talent matching and benchmarking platform that maps candidate capabilities against industry job descriptions and company hiring bars across **12 RADIX skill categories** and workplace alignment parameters.

---

## 🏗️ Architecture & 5-Role Team Distribution

This repository is structured so all **5 team members** can develop their assigned modules in parallel without merge conflicts or blockers:

```
radix-talent-match/
├── .gitignore                          # Standard Node & Python exclusions
├── README.md                           # Team guide and architecture documentation
├── RADIX_Talent_Match_Team_Tracker.csv # 20-milestone sprint tracker with time allocations
│
├── data/
│   ├── contracts/
│   │   └── shared_data_contract.json   # Official JSON schema connecting all 5 roles
│   └── mocks/
│       ├── mock_candidate_profile.json # Mock candidate profile (Ananya Rao)
│       ├── mock_jd_skills.json         # Mock parsed Google SWE JD
│       └── talent_check_company_skillsets.json # Google, Microsoft, Oracle benchmarks (1-10)
│
├── frontend/                           # Owned by Role 3 (Scrum Master / Frontend Lead)
│   ├── README.md                       # Lovable UI mounting & dev instructions
│   └── src/
│       └── lib/
│           └── error-capture.ts        # Out-of-band error & stack capture utility
│
└── backend/
    ├── requirements.txt                # FastAPI, uvicorn, langchain, pypdf, python-docx
    ├── main.py                         # Unified API gateway mounting all role routers
    │
    ├── role1_jd_analytics/             # Owned by Member 1
    │   ├── extractor.py                # LLM JD extraction onto 12 RADIX categories
    │   ├── router.py                   # POST /api/v1/jd/extract
    │   └── README.md
    │
    ├── role2_resume_parsing/           # Owned by Member 2
    │   ├── parser.py                   # LLM Resume parsing into CandidateProfile
    │   ├── router.py                   # POST /api/v1/resume/parse
    │   └── README.md
    │
    ├── role4_talent_check/             # Owned by Member 4
    │   ├── scorer.py                   # 12-category company benchmark scoring engine
    │   ├── router.py                   # GET /companies, POST /api/v1/talent-check/evaluate
    │   └── README.md
    │
    └── role5_skill_matching/           # Owned by Member 5
        ├── matcher.py                  # Gap analysis, fit %, and HIGH/MED/LOW recommendations
        ├── router.py                   # POST /api/v1/skills/match
        └── README.md
```

---

## 👥 Team Responsibilities & Ownership Matrix

| Role | Domain / Module | Path | Primary Responsibilities |
| :--- | :--- | :--- | :--- |
| **Role 1** | **JD Analytics** | `backend/role1_jd_analytics/` | Map PDF/DOCX job descriptions onto the 12 RADIX skill categories and workplace parameters. |
| **Role 2** | **Resume Parsing** | `backend/role2_resume_parsing/` | Parse CVs/resumes into standardized 1-10 proficiency profiles with evidence quotes. |
| **Role 3** | **Frontend Lead** | `frontend/` | Integrate Lovable React UI, mount Candidate Profile Builder, and connect API endpoints. |
| **Role 4** | **Talent Check** | `backend/role4_talent_check/` | Benchmark candidate proficiency against Google, Microsoft, and Oracle hiring bars. |
| **Role 5** | **Skill Matching** | `backend/role5_skill_matching/` | Calculate JD-vs-Candidate fit %, detect missing skills, and output prioritized gap fixes. |

---

## 📊 The 12 RADIX Skill Categories & Extended Parameters

All models, parsers, and UI components evaluate candidates across these exact 12 categories:
1. `Core Technical Skills`
2. `Software Architecture & Design`
3. `Systems & Cloud Infrastructure`
4. `Data Engineering & Databases`
5. `Quality Assurance & Testing`
6. `Security & Compliance`
7. `Developer Tooling & DevOps`
8. `Problem Solving & Algorithms`
9. `Collaboration & Communication`
10. `Project & Product Management`
11. `Business Domain & Industry Knowledge`
12. `Learning & Adaptability`

### Extended Workplace Parameters
- **Parameter 164 (Communication Style):** Async-first RFCs vs Sync-heavy standups.
- **Parameter 165 (Pacing & Autonomy):** High-ownership iterative sprints vs structured gatekeeping.
- **Parameter 166 (Collaboration Breadth):** Cross-functional global pods vs siloed engineering teams.

---

## ⚡ Quickstart Guide

### 1. Backend Setup (Roles 1, 2, 4, 5)

```bash
# 1. Create and activate a Python virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# 2. Install dependencies
pip install -r backend/requirements.txt

# 3. Start the FastAPI development server
uvicorn backend.main:app --reload --port 8000
```
- Interactive Swagger API Documentation: [http://localhost:8000/docs](http://localhost:8000/docs)
- Health check: [http://localhost:8000/health](http://localhost:8000/health)

### 2. Frontend Setup (Role 3 / Lovable Integration)

```bash
cd frontend
npm install
npm run dev
```
- Open [http://localhost:5173](http://localhost:5173) in your browser.
- Configure backend API base URL in `frontend/.env.local`:
  ```env
  VITE_API_BASE_URL=http://localhost:8000
  ```

---

## 🔄 Git Branching Strategy (Zero Conflicts)

Each team member works in their dedicated branch and submits pull requests:

```bash
# Create and switch to your feature branch
git checkout -b feature/role1-jd-analytics   # Member 1
git checkout -b feature/role2-resume-parser   # Member 2
git checkout -b feature/role3-lovable-ui      # Member 3
git checkout -b feature/role4-talent-check    # Member 4
git checkout -b feature/role5-skill-matching  # Member 5

# Stage and commit only your module files
git add backend/role1_jd_analytics/
git commit -m "feat(role1): integrate LLM extraction prompt for 12 RADIX categories"
git push origin feature/role1-jd-analytics
```

---

## 📄 License & Attribution
Developed for the **Talentia Global Agentic AI & Coding Challenges Bootcamp**.
