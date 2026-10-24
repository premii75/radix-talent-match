"""
FastAPI Router for Role 1: JD Analytics
Endpoints:
- POST /api/v1/jd/extract (upload PDF/DOCX or send JSON payload)
"""

from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from typing import Optional
import tempfile
import os
from .extractor import JDExtractor

router = APIRouter(prefix="/api/v1/jd", tags=["Role 1 - JD Analytics"])
extractor = JDExtractor()

@router.post("/extract")
async def extract_jd(
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
                result = extractor.extract_from_file(tmp_path)
            finally:
                if os.path.exists(tmp_path):
                    os.remove(tmp_path)
            return result

        if raw_text:
            return extractor.extract_from_text(raw_text)

        # Fallback if empty request
        return extractor._load_fallback_mock()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
