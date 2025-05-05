from agents import Agent, Runner, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel
import os
import json
set_tracing_disabled(disabled=True)
API_KEY= os.getenv('GEMINI_API_KEY') 
# print(API_KEY)
MODEL : str = os.getenv('MODEL')
# print(MODEL)
async def _generate_question()-> str:
    agent = Agent(
        name = 'Question Generator',
        instructions="You are a quiz-generating agent specialized in Python programming and the OpenAI Agents SDK.",
        model=LitellmModel(model=MODEL,api_key=API_KEY)
    )
    QUESTION = await Runner.run(agent,"Generate a single multiple-choice question (MCQ) related to either Python programming or the OpenAI Agents SDK.")
    return QUESTION.final_output
