import random
choices = ["rock", "paper", "scissors"]
count = 0
user_wins = 0
comp_wins = 0
while True:
    count += 1
    in_put = input("Type Rock / Paper /Scissors or Q to quit ").lower()
    if in_put == "q":
        break
    elif in_put not in choices:
        continue
    rd = random.randint(0, 2)
    compinput = choices[rd]
    if in_put == "rock" and compinput == "scissors":
        print("Computer picked scissors, you win")
        user_wins += 1
    elif in_put == "paper" and compinput == "rock":
        print("Computer picked rock, you win")
        user_wins += 1
    elif in_put == "scissors" and compinput == "paper":
        print("Computer picked paper, you win")
        user_wins += 1
    else:
        print("You lost try again")
        comp_wins += 1
    if count == 3:
        break
print("Out of 3 you had", user_wins)
if user_wins < 2:
    print("You lost!")
else:
    print("You beat your PC :)")

