import random
guesses = 0
while True:
    guesses += 1
    random_guess = input("Enter a random number... ")
    if random_guess.isdigit():
        random_guess = int(random_guess)
    else:
        print("Enter a number next time :)")
        continue
    r = random.randint(0, random_guess)
    if random_guess == r:
        print("Congratulations you got it right!")
        break
    elif random_guess > r:
            print("oops...just above it")
    else:
            print("just below it! keep going.")
print("after " + str(guesses) + " times")