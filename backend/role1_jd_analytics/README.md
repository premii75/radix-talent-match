# Role 1: JD Analytics Module

**Assigned Member:** Member 1  
**Scope:** Extract structured skill requirements from PDF, DOCX, or raw JD text and map them into the 12 RADIX categories + workplace parameters.

---

## 🛠️ Responsibilities & Tasks
1. Complete `extractor.py` using LangChain / OpenAI / Google Gemini prompt engineering.
2. Ensure prompt maps natural language requirements onto the exact 12 RADIX categories:
   - *Core Technical Skills*
   - *Software Architecture & Design*
   - *Systems & Cloud Infrastructure*
   - *Data Engineering & Databases*
   - *Quality Assurance & Testing*
   - *Security & Compliance*
   - *Developer Tooling & DevOps*
   - *Problem Solving & Algorithms*
   - *Collaboration & Communication*
   - *Project & Product Management*
   - *Business Domain & Industry Knowledge*
   - *Learning & Adaptability*
3. Extract workplace parameters (Communication style, work pacing, collaboration breadth).
4. Verify response adheres to `data/contracts/shared_data_contract.json#definitions/JDSkillExtraction`.

---

## 🧪 Testing Locally
```bash
# Run unit test or test endpoint directly
curl -X POST http://localhost:8000/api/v1/jd/extract \
  -F "raw_text=Looking for Senior Python & Go Developer with 5 years Kubernetes and Distributed Systems experience"
```
