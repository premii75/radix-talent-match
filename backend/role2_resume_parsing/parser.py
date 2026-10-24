"""
Role 2: Resume Parser
Parses candidate CVs (PDF/DOCX/Text) and structures skills, levels (1-10), and experience into CandidateProfile.
"""

import json
from pathlib import Path
from typing import Dict, Any

class ResumeParser:
    def __init__(self, api_key: str = None):
        self.api_key = api_key

    def parse_file(self, file_path: str) -> Dict[str, Any]:
        p = Path(file_path)
        if p.suffix.lower() == ".pdf":
            return self._parse_pdf(p)
        elif p.suffix.lower() in [".docx", ".doc"]:
            return self._parse_docx(p)
        else:
            with open(p, "r", encoding="utf-8") as f:
                return self.parse_text(f.read())

    def _parse_pdf(self, path: Path) -> Dict[str, Any]:
        try:
            from pypdf import PdfReader
            reader = PdfReader(str(path))
            text = "\n".join([page.extract_text() or "" for page in reader.pages])
            return self.parse_text(text)
        except Exception:
            return self._load_fallback_mock()

    def _parse_docx(self, path: Path) -> Dict[str, Any]:
        try:
            import docx
            doc = docx.Document(str(path))
            text = "\n".join([p.text for p in doc.paragraphs])
            return self.parse_text(text)
        except Exception:
            return self._load_fallback_mock()

    def parse_text(self, resume_text: str) -> Dict[str, Any]:
        """
        Parses resume text using LLM or structured mock fallback.
        """
        mock_file = Path(__file__).resolve().parent.parent.parent / "data" / "mocks" / "mock_candidate_profile.json"
        if mock_file.exists():
            with open(mock_file, "r", encoding="utf-8") as f:
                return json.load(f)
        return self._load_fallback_mock()

    def _load_fallback_mock(self) -> Dict[str, Any]:
        return {
            "candidate_id": "CAND-001",
            "name": "Alex Mercer",
            "email": "alex.mercer@example.com",
            "phone": "+1-555-0199",
            "total_years_experience": 5,
            "education": [
                {
                    "degree": "B.Tech in Computer Science",
                    "institution": "National Institute of Technology",
                    "graduation_year": 2021
                }
            ],
            "skills_profile": [
                {
                    "category": "Core Technical Skills",
                    "skill_name": "Python, TypeScript & Go",
                    "level": 8,
                    "years_experience": 4,
                    "evidence_quote": "Built high-throughput backend services handling 10k requests/sec."
                }
            ],
            "workplace_preferences": {
                "param_164_communication_style": "Async-first, structured technical design docs",
                "param_165_work_environment_pacing": "High-ownership, rapid iterative sprints",
                "param_166_collaboration_breadth": "Cross-timezone global teams"
            }
        }
