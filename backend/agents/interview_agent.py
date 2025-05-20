
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from backend.prompts.interview_prompt import INTERVIEW_PROMPT_TEMPLATE

llm = ChatOpenAI(temperature=0.7, model="gpt-3.5-turbo")

interview_prompt = PromptTemplate(
    input_variables=["company_name", "job_description", "research_summary", "previous_answer"],
    template=INTERVIEW_PROMPT_TEMPLATE
)

interview_chain = LLMChain(llm=llm, prompt=interview_prompt)

def run_interview_agent(company_name: str, job_description: str, research_summary: str, previous_answer: str) -> str:
    print("🗣️ Interview agent generating next question...")
    response = interview_chain.run({
        "company_name": company_name,
        "job_description": job_description,
        "research_summary": research_summary,
        "previous_answer": previous_answer
    })
    print("✅ Interview question generated.")
    return response