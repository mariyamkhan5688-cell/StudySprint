 StudySprint Main Menu

import quiz


def main():
    while True:
        print()
        print("=== StudySprint ===")
        print("1. Start Quiz")
        print("2. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            quiz.run_quiz()
        elif choice == "2":
            print("Thanks for using StudySprint!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
