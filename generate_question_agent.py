from agents import Agent, Runner, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel
import os
import json
set_tracing_disabled(disabled=True)
API_KEY= os.getenv('GEMINI_API_KEY') 
# print(API_KEY)
MODEL : str = os.getenv('MODEL')
# print(MODEL)
async def _generate_question(difficultiy_leve: str)-> str:
    agent = Agent(
        name = 'Question Generator',
        instructions=f"You are a quiz-generating agent specialized in Python programming and the OpenAI Agents SDK.",
        model=LitellmModel(model=MODEL,api_key=API_KEY)
    )
    QUESTION = await Runner.run(agent,f"Generate a single multiple-choice question (MCQs) related to either Python programming or the OpenAI Agents SDK. User difficulty is {difficultiy_leve}, don't repeat the question.")
    return QUESTION.final_output
