import random

choices = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0

def get_user_choice():
    while True:
        choice = input("Choose Rock, Paper, or Scissors: ").lower()
        if choice in choices:
            return choice
        print("Invalid choice. Try again.")

def get_computer_choice():
    return random.choice(choices)

def decide_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def play_round():
    global user_score, computer_score
    print("\n--- Rock Paper Scissors ---")
    user = get_user_choice()
    computer = get_computer_choice()
    print(f"You chose: {user}")
    print(f"Computer chose: {computer}")
    
    winner = decide_winner(user, computer)
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        computer_score += 1
    
    print(f"Score -> You: {user_score} | Computer: {computer_score}")

def main():
    print("🎮 Welcome to Rock, Paper, Scissors Game!")
    while True:
        play_round()
        again = input("\nPlay again? (yes/no): ").lower()
        if again != "yes":
            print("Thanks for playing!")
            break

main()
