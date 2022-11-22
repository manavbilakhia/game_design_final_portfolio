# I affirm that I have carried out my academic endeavors with full academic honesty.
# @MB (Manav Bilakhia)
# read the readme file for more information on how to run this script
import random
def play():
    secret_number = random.randint(1, 100)
    print("I have chosen a secret number between 1 and 100. What number is it?")
    guess = int(input("Please make a guess. "))
    while guess != secret_number: #gameloop
        if guess < secret_number:
            guess = int(input("My number is higher than that. Try again. "))
        elif guess > secret_number:
            guess = int(input("My number is lower than that. Try again. "))
    print("Yay! You guessed it. My secret number was!" + str(secret_number))

play()

