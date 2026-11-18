# StudySprint Quiz System

questions = [
    {
        "question": "What is the powerhouse of the cell?",
        "choices": ["A. Nucleus", "B. Mitochondria", "C. Ribosome", "D. Cell membrane"],
        "answer": "B"
    },
    {
        "question": "What planet is known as the Red Planet?",
        "choices": ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"],
        "answer": "C"
    },
    {
        "question": "What is 12 x 12?",
        "choices": ["A. 124", "B. 144", "C. 154", "D. 164"],
        "answer": "B"
    }
]


def run_quiz():
    score = 0

    print("=== StudySprint Quiz ===")
    print()

    for number, question in enumerate(questions, start=1):
        print(f"Question {number}: {question['question']}")

        for choice in question["choices"]:
            print(choice)

        user_answer = input("Your answer: ").strip().upper()

        if user_answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {question['answer']}.")

        print()

    print("=== Quiz Complete ===")
    print(f"Your score: {score}/{len(questions)}")


if __name__ == "__main__":
    run_quiz()
