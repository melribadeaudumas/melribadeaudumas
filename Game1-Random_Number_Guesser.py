import random

print("Hello in this game you need to guess the number between 0 and 100 I am thinking about")

number = random.randint(0, 100)
guess = 0

while guess != number:
    print("Please enter your guess")
    guess = int(input())
    if guess < number:
        print("The number I am thinking about is bigger")
    elif guess > number:
        print("The number I am thiking about is smaller")
    else:
        print("that's the right number !")

