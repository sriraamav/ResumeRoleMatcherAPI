from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from utils.parser import extract_text_from_pdf
from utils.skills_extractor import extract_skills_from_text
import shutil
import os

app = FastAPI()

@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    try:
        # Save uploaded file temporarily
        temp_path = f"temp_{file.filename}"
        with open(temp_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Extract text
        resume_text = extract_text_from_pdf(temp_path)

        # Clean up temp file
        os.remove(temp_path)

        if not resume_text:
            return JSONResponse(status_code=400, content={"error": "Could not extract text from resume."})

        # Match skills
        matches = extract_skills_from_text(resume_text)

        # Sort by score and return
        sorted_roles = sorted(matches.items(), key=lambda x: x[1]['score'], reverse=True)
        return {"matches": sorted_roles}

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
