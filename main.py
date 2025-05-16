import json
from time import sleep
from evaluate_answer_agent import _evaluate_answer_agent
from generate_question_agent import _generate_question
import chainlit as cl

@cl.on_chat_start
async def on_start():
    test_message : str = """
    - Total Questions = 10
    - Passing Question/Marks = 7
    - The programe will adjust difficulty according to your correct answers
    - Means difficulty is Directly Proportional to correct answers.
    - The Program will Automatically stop after 10 Questions.

    Type Start to Initiate the Test/Exam in Open AI Agent SDK, Python Programming
    
"""
 
    await cl.Message(content=test_message).send()

@cl.on_message
async def on_message(message: cl.Message):
    if message.content.lower() == "start":
        await cl.Message("Starting the test...").send()
        # Add your test logic here
    else:
        await cl.Message("Type 'start' to begin the test").send()
