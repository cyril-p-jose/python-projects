import random

print("WELCOME TO THE NUMBER GUESSING GAME")
print("-----------------------------------")
print("I have chosen a number between 1 and 10")

number = random.randint(1, 10)

while True:
    guess = int(input("Enter your guess: "))

    if guess == number:
        print("Congratulations! You guessed the correct number.")
        break
    elif guess < number:
        print("Too small.")
    else:
        print("Too large.")
