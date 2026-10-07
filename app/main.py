from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse

from app.parsepdf import parse_pdf
from app.agents.resume_extractor import extract_resume_data as analyze_resume
from app.agents.jd_extractor import analyze_jd
from app.agents.candidate_evaluation import evaluate_candidate

import json

app = FastAPI()


@app.post("/screening/")
async def upload_resume(
    resume: UploadFile = File(...),
    jd: UploadFile = File(...)
):
    print("Received resume:", resume.filename)
    print("Received JD:", jd.filename)

    # -------------------------
    # Parse Resume
    # -------------------------
    resume_text = parse_pdf(resume.file)

    candidate_details = analyze_resume(resume_text)

    print("Candidate details:", candidate_details)

    # -------------------------
    # Parse Job Description
    # -------------------------
    jd_text = parse_pdf(jd.file)

    jd_details = analyze_jd(jd_text)

    print("JD details:", jd_details)

    # -------------------------
    # Evaluate Candidate
    # -------------------------
    evaluation = evaluate_candidate(
        candidate_details,
        jd_details
    )

    print("Evaluation result:", evaluation)

    # -------------------------
    # Return JSON response
    # -------------------------
    result_json = json.loads(evaluation)

    return JSONResponse(content=result_json)