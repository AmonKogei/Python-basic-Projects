print("Welcome To The IQ Test")
score = 0
print("Let's Start with your name shall we?")
Subject = input()
if Subject == "":
    quit("Sorry Bye!")
else:
    print("Hello " + Subject + " ! Let's begin.")
Answer = input("Can a cow drive a plane? ").lower()
if Answer == "no":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
Answer = input("Can a fish fly? ").lower()
if Answer == "no":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

Answer = input("Are you a cow? ").lower()
if Answer == "no":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
if score >= 2:
    print("Great job! Your score is " + str((score/3) * 100) + "%")
else:
    print("Your score was " + str((score/3) * 100) + "% you shouldn't be here :(")
