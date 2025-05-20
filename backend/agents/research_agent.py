# backend/agents/research_agent.py

import os
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from backend.prompts.research_prompt import RESEARCH_PROMPT_TEMPLATE

llm = ChatOpenAI(
    temperature=0.7,
    model="gpt-3.5-turbo"
)

research_prompt = PromptTemplate(
    input_variables=["company_name", "job_description"],
    template=RESEARCH_PROMPT_TEMPLATE
)

research_chain = LLMChain(llm=llm, prompt=research_prompt)

def run_research_agent(company_name: str, job_description: str) -> str:
    print("🔎 Running research agent...")
    response = research_chain.run({
        "company_name": company_name,
        "job_description": job_description
    })
    print("✅ Research response complete.")
    return response