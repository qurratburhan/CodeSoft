import random
def user_choice1():
    print('WELCOME BACK!!!!')
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        user_choice = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()
    return user_choice
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
            (user_choice == 'scissors' and computer_choice == 'paper') or \
            (user_choice == 'paper' and computer_choice == 'rock'):
        return "user"
    else:
        return "computer"


def display_result(user_choice, computer_choice, winner):
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win!")
    else:
        print("Computer wins!")


def play_again():
    play_more = input("Do you want to play another round? (yes/no): ").lower()
    return play_more == 'yes'


def main():
    user_score = 0
    computer_score = 0

    print("Rock-Paper-Scissors!")

    while True:
        user_choice = user_choice1()
        computer_choice = computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, winner)

        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1

        print(f"Score - You: {user_score}, Computer: {computer_score}")

        if not play_again():
            break
    print("Thank you for playing! Final Score - You: {user_score}, Computer: {computer_score}")

if __name__ == "__main__":
    main()
