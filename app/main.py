from fastapi import FastAPI
from app.schemas import MatchRequest, MatchResponse
from app.services.matcher import match_resume_to_jd

app = FastAPI(title="Resume Job Matcher")


@app.get("/")
def read_root():
    return {"message": "Resume Job Matcher API is running"}


@app.post("/match", response_model=MatchResponse)
def match_endpoint(payload: MatchRequest):
    return match_resume_to_jd(
        resume_text=payload.resume_text,
        jd_text=payload.job_description,
    )