import json
from evaluate_answer_agent import _evaluate_answer_agent
from generate_question_agent import _generate_question
import asyncio
from user_test_history import _get_correct_answers, _get_incorrect_answers, _get_user_test_history

async def main():
    # Load existing counters from questions.json
    try:
        with open('questions.json', 'r') as f:
            questions = json.load(f)
            if questions:
                # Get the most recent counts from the last question
                last_question = questions[-1]
                correct_ans = last_question['correct_answers']
                incorrect_ans = last_question['incorrect_answers']
            else:
                correct_ans = 0
                incorrect_ans = 0
    except FileNotFoundError:
        questions = []
        correct_ans = 0
        incorrect_ans = 0

    print("Hello from mcqs-agent!")
    print(f"Current correct answers: {correct_ans}")
    print(f"Current incorrect answers: {incorrect_ans}")
    
    question = await _generate_question()
    print(question)
    answer = input("You:->")
    final_answer = await _evaluate_answer_agent(single_question=question, user_answer=answer)
    print(final_answer)

    # Update counters based on the answer
    if final_answer.strip() == "Correct":
        correct_ans += 1
    elif final_answer.strip() == "Incorrect":
        incorrect_ans += 1

    new_question = {
        'serial_number': len(questions) + 1,
        'correct_answers': correct_ans,
        'incorrect_answers': incorrect_ans,
        'question_data': {
            'question': question,
            'user_answer': answer,
            'evaluation': final_answer
        }
    }
    print(new_question)
    questions.append(new_question)

    with open('questions.json', 'w') as f:
        json.dump(questions, f, indent=4)
        print("Question data saved successfully")
        print(f"Total correct answers: {correct_ans}")
        print(f"Total incorrect answers: {incorrect_ans}")

if __name__ == "__main__":
    asyncio.run(main())