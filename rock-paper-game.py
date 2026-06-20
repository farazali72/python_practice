import random

item_list = ["Rock", "Paper", "Scissor"]

user_choice = input("Enter your move = Rock, Paper, Scissor: ").strip().capitalize()
comp_choice = random.choice(item_list)

print(f"User choice = {user_choice}")
print(f"Computer choice = {comp_choice}")

if user_choice not in item_list:
    print("Invalid input! Please enter Rock, Paper or Scissor.")

elif user_choice == comp_choice:
    print("Both chose same: Match is tied")

elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper covers Rock = computer wins the match")
    else:
        print("Rock smashes Scissor = you win the match")

elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Scissor cuts Paper = computer wins the match")
    else:
        print("Paper covers Rock = you win the match")

elif user_choice == "Scissor":
    if comp_choice == "Rock":
        print("Rock breaks Scissor = computer wins the match")
    else:
        print("Scissor cuts Paper = you win the match")