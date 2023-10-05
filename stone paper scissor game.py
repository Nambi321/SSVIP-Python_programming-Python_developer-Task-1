import random


# We write the Function to get the user's choice
def get_user_choice():
    user_choice = input("Enter your choice (Stone, Paper, or Scissors): ")
    while user_choice not in ["Stone", "Paper", "Scissors"]:
        print("Sorry!! Please Enter Stone, Paper, or Scissors Only.")
        user_choice = input("Enter your choice (Stone, Paper, or Scissors): ")
    return user_choice


# We write the Function to generate the computer's choice
def get_comp_choice():
    choices = ["Stone", "Paper", "Scissors"]
    comp_choice = random.choice(choices)
    return comp_choice


# We write the Function to determine the winner
def determine_winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        return "The Game is Tie!"
    elif (
        (user_choice == "Stone" and comp_choice == "Scissors")
        or (user_choice == "Paper" and comp_choice == "Stone")
        or (user_choice == "Scissors" and comp_choice == "Paper")
    ):
        return "Hurray!! You win the Match"
    else:
        return "Oops! Computer wins! No worries let's Play Again"


# We write the Main game loop
while True:
    user_choice = get_user_choice()
    comp_choice = get_comp_choice()

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {comp_choice}")

    result = determine_winner(user_choice, comp_choice)
    print(result)

    play_again = input("Wanna Play Again? (Yeah/Nope): ")
    if play_again != "Yeah":
        break
