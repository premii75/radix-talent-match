"""
FastAPI Router for Role 2: Resume Parsing
Endpoints:
- POST /api/v1/resume/parse (upload PDF/DOCX or send text)
"""

from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from typing import Optional
import tempfile
import os
from .parser import ResumeParser

router = APIRouter(prefix="/api/v1/resume", tags=["Role 2 - Resume Parsing"])
parser = ResumeParser()

@router.post("/parse")
async def parse_resume(
    file: Optional[UploadFile] = File(None),
    raw_text: Optional[str] = Form(None)
):
    try:
        if file:
            suffix = os.path.splitext(file.filename)[1]
            with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
                content = await file.read()
                tmp.write(content)
                tmp_path = tmp.name

            try:
                result = parser.parse_file(tmp_path)
            finally:
                if os.path.exists(tmp_path):
                    os.remove(tmp_path)
            return result

        if raw_text:
            return parser.parse_text(raw_text)

        return parser._load_fallback_mock()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
