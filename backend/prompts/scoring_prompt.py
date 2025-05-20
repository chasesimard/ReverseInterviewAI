
SCORING_PROMPT_TEMPLATE = """
You are a senior hiring manager evaluating a candidate's interview performance.

Given the following inputs:
- Job Description
- Company Research Summary
- Full Interview Transcript (Q&A)

Assign a score (0–100) for overall interview quality and include a 3–5 sentence evaluation summary.

Job Description:
{job_description}

Company Research:
{research_summary}

Interview Transcript:
{interview_transcript}

Return your response as:
Score: <number>
Summary: <detailed feedback>
"""