import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from backend.agents.research_agent import run_research_agent
from backend.agents.interview_agent import run_interview_agent
from backend.agents.scoring_agent import run_scoring_agent

app = FastAPI()

# Fix CORS issue
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict to ["http://localhost:5173"] later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"status": "API is running"}

@app.post("/research")
def research(
    company: str = Body(...),
    job: str = Body(...)
):
    result = run_research_agent(company_name=company, job_description=job)
    return {"research_summary": result}

@app.post("/interview")
def interview(
    company: str = Body(...),
    job: str = Body(...),
    research: str = Body(...),
    answer: str = Body(default="")
):
    result = run_interview_agent(
        company_name=company,
        job_description=job,
        research_summary=research,
        previous_answer=answer
    )
    return {"next_question": result}

@app.post("/score")
def score(
    job: str = Body(...),
    research: str = Body(...),
    transcript: str = Body(...)
):
    result = run_scoring_agent(
        job_description=job,
        research_summary=research,
        interview_transcript=transcript
    )
    return {"interview_score": result}