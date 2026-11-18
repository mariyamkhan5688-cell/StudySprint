
flashcards = [
    {
        "question": "What is the powerhouse of the cell?",
        "answer": "The mitochondria."
    },
    {
        "question": "What planet is known as the Red Planet?",
        "answer": "Mars."
    },
    {
        "question": "What is 12 x 12?",
        "answer": "144."
    }
]


def show_flashcards():
    print("=== StudySprint Flashcards ===")
    print()

    for number, card in enumerate(flashcards, start=1):
        print(f"Card {number}:")
        print("Question:", card["question"])

        input("Press Enter to reveal the answer...")

        print("Answer:", card["answer"])
        print("-" * 30)


if __name__ == "__main__":
    show_flashcards()
