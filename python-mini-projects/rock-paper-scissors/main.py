from random import randint

def main():
    choices = {1: "Rock", 2: "Paper", 3: "Scissor"}
    score = 0
    attempts = 0

    while True:
        try:
            your_choice = int(input("\n1. Rock, 2. Paper, 3. Scissor, 4. Exit: "))
            if your_choice == 4:
                break
            if your_choice in {1, 2, 3}:
                attempts -= (1)

            computer_choice = randint(1, 3)
            attempts += 1
            print(
                f"You choose {choices[your_choice]} and computer chose {choices[computer_choice]}"
            )

            if your_choice == computer_choice:
                print("It's a draw.")
                attempts -= 1
            elif str(your_choice) + str(computer_choice) in ["13", "21", "32"]:
                print("You win")
                score += 1
            else:
                print("You lose.")
        except:
            print("Invalid choice.")
            break
    print(f"Your score is {score}/{attempts}")
    print("Thanks for playing")

if __name__ == "__main__":
    main()
