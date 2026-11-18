def main():
    print("Welcome to StudySprint!")
    print()
    print("1. Flashcards")
    print("2. Quiz")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("Flashcards selected.")
    elif choice == "2":
        print("Quiz selected.")
    elif choice == "3":
        print("Goodbye!")
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
