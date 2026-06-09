import random

questions = [
    {"question": "What is the capital of Nigeria? ", "answer": "Abuja"},
    {"question": "What is 10 + 10?", "answer": "20"},
    {"question": "What language are you learning?", "answer": "Python"},
    {"question": "What is the capital of Ghana?", "answer": "Accra"},
    {"question": "What is 5 x 5?", "answer": "25"}
]


selected = random.sample(questions, 3)
score = 0 

for q in selected:
        answer = input(q["question"] + "")
        if answer.lower() == q["answer"].lower():
                print("Correct ")
                score += 1

        else:
                print("Wrong! The answer is:", q["answer"])

print("Score:", score, "/3")                        
