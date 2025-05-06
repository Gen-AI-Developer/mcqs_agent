from agents import Agent, Runner, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel
import os
import json
set_tracing_disabled(disabled=True)
API_KEY= os.getenv('GEMINI_API_KEY') 
# print(API_KEY)
MODEL : str = os.getenv('MODEL')
# print(MODEL)
async def _generate_question(difficultiy_level: str,question_history: list = None) -> str:
    # Add instruction to avoid previously asked questions
    """
    Function: _generate_question
    Arg: difficulty_level : str
    Arg: question history : str
    return : str (a single question)
    """
    # print(difficultiy_level)
    # print(question_history)

    history_instruction = ""
    if question_history:
        history_instruction = "\nAvoid these previously asked questions:\n" + "\n".join(question_history)
    
    agent = Agent(
        name="Question Generator",
        instructions=f"You are a quiz-generating agent specialized in Python programming and the OpenAI Agents SDK. Generate unique questions that haven't been asked before.{history_instruction}",
        model=LitellmModel(model=MODEL, api_key=API_KEY)
    )
    
    QUESTION = await Runner.run(agent, f"Generate a single multiple-choice question (MCQ) related to either Python programming or the OpenAI Agents SDK. with difficulty level of {difficultiy_level}")
    return QUESTION.final_output