import json
from evaluate_answer_agent import _evaluate_answer_agent
from generate_question_agent import _generate_question  # Import the specific function
import asyncio
from user_test_history import _get_correct_answers, _get_incorrect_answers, _get_user_test_history

async def main():
    print("Hello from mcqs-agent!")
    # test_history : dict = _get_user_test_history()
    question = await _generate_question()  # Now this should work
    print(question)
    answer = input("You:->")
    final_answer = await _evaluate_answer_agent(single_question=question,user_answer=answer)
    print(final_answer)
    try:
        with open('questions.json', 'r') as f:
            questions = json.load(f)
    except FileNotFoundError:
        questions = []

    serial_number = len(questions) + 1
    new_question = {
        'serial_number': serial_number,
        'correct_answers': _get_correct_answers,
        'incorrect_answers': _get_incorrect_answers,
        questions : {
            'question':question,
        }
    }
    questions.append(new_question)

    with open('questions.json', 'w') as f:
        json.dump(questions, f, indent=4)
        print("file Questio Sved")
    # return question

if __name__ == "__main__":
    asyncio.run(main())