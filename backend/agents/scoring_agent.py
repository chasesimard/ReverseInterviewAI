
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from backend.prompts.scoring_prompt import SCORING_PROMPT_TEMPLATE

llm = ChatOpenAI(temperature=0.3, model="gpt-3.5-turbo")

scoring_prompt = PromptTemplate(
    input_variables=["job_description", "research_summary", "interview_transcript"],
    template=SCORING_PROMPT_TEMPLATE
)

scoring_chain = LLMChain(llm=llm, prompt=scoring_prompt)

def run_scoring_agent(job_description: str, research_summary: str, interview_transcript: str) -> str:
    print("📊 Running scoring agent...")
    response = scoring_chain.run({
        "job_description": job_description,
        "research_summary": research_summary,
        "interview_transcript": interview_transcript
    })
    print("✅ Score and feedback generated.")
    return response