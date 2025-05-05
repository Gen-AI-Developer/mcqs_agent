# import asyncio
from agents import Agent, Runner, set_tracing_disabled
import os
from agents.extensions.models.litellm_model import LitellmModel
api_key = os.getenv('GEMINI_API_KEY')
set_tracing_disabled(disabled=True)
MODEL='gemini/gemini-2.0-flash'
async def _evaluate_answer_agent(single_question:str, user_answer: str) -> str:
    agent = Agent(name="Question Evaluator",instructions="Your are Expert in Open AI Agent SDK and Python Programming, You are good at Question Evaluation  and then Answer it in simple Two Word Correct / Incorrect.",model=LitellmModel(model=MODEL,api_key=api_key))
    query = f"This is question : {single_question} for evaluation, and this is the user answer: {user_answer}"
    output = await Runner.run(agent,query)
    return output.final_output

# async def main():
#     result = await _evaluate_answer_agent('What is Python?', 'Python is a programming language')
#     print(result)

# if __name__ == "__main__":
#     asyncio.run(main())