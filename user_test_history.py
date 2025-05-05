import json


def _get_user_test_history():
    pass
def _get_correct_answers():
    correctAnswer= 0
    try:
        with open('question.json','r') as f:
            data = json.load(f)
            if not data:
                return 0
            else:
                correctAnswer = data['correct_answers']
    except FileNotFoundError:
        return 0

    return correctAnswer
def _get_incorrect_answers():
    incorrectAnswer= 0
    try:
        with open('question.json','r') as f:
            data = json.load(f)
            if not data:
                return 0
            else:
                incorrectAnswer = data['incorrect_answers']
    except FileNotFoundError:
        return 0
    return incorrectAnswer