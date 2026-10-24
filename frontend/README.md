# Frontend Workspace (Lovable / React UI)

**Owner:** Role 3 (Scrum Master / Frontend Lead)  
**Integrated Service:** Lovable Generated UI + RADIX Profile Builder

---

## 🚀 Setup & Lovable Integration Guide

1. **Export from Lovable:**
   - Download or sync your Lovable project files into this `frontend/` directory.
   - Keep `src/lib/error-capture.ts` intact (it captures unhandled exceptions and full cause stacks for seamless debugging).

2. **Installation:**
   ```bash
   cd frontend
   npm install
   ```

3. **Environment Setup:**
   Create `.env.local` inside `frontend/`:
   ```env
   VITE_API_BASE_URL=http://localhost:8000
   ```

4. **Running Locally:**
   ```bash
   npm run dev
   ```
   Open [http://localhost:5173](http://localhost:5173) in your browser.

---

## 📡 API Endpoints Consumed by Frontend

| Feature | HTTP Method | Backend Endpoint | Source Role |
| :--- | :--- | :--- | :--- |
| **JD Skill Extraction** | `POST` | `/api/v1/jd/extract` | Role 1 |
| **Resume Parsing** | `POST` | `/api/v1/resume/parse` | Role 2 |
| **Talent Check / Company Fit** | `POST` | `/api/v1/talent-check/evaluate` | Role 4 |
| **Skill Match & Gap Analysis**| `POST` | `/api/v1/skills/match` | Role 5 |

Mock JSON data for offline development is located in `../data/mocks/`.
