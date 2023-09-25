import random


# We write the Function to get the user's choice
def get_user_choice():
    user_choice = input("Enter your choice (Stone, Paper, or Scissors): ")
    while user_choice not in ["Stone", "Paper", "Scissors"]:
        print("Sorry!! Please Enter Stone, Paper, or Scissors Only.")
        user_choice = input("Enter your choice (Stone, Paper, or Scissors): ")
    return user_choice


# We write the Function to generate the computer's choice
def get_computer_choice():
    choices = ["Stone", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    return computer_choice


# We write the Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "The Game is Tie!"
    elif (
        (user_choice == "Stone" and computer_choice == "Scissors")
        or (user_choice == "Paper" and computer_choice == "Stone")
        or (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        return "Hurray!! You win the Match"
    else:
        return "Oops! Computer wins! No worries let's Play Again"


# We write the Main game loop
while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)

    play_again = input("Wanna Play Again? (Yeah/Nope): ")
    if play_again != "Yeah":
        break
