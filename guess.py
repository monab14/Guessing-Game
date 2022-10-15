import random

print("WELCOME TO THE GUESSING GAME")
name =input("Enter your name: ")
age=input("Enter your age: ")

print(f"Hello {name} Please guess a number from 1 to 100 in 5 seconds.\nGuess Smartly you have only 10 chances\nGood Luck!!!")

print(f"Pick a number {name}...")

guess =int(input(f"What is your guess {name} : "))
correct=random.randint(1,50)
guess_count=(10)

while guess !=correct:
    guess_count-=1
    if guess<correct:
        guess=int(input(f"No dear! Your number is lower Guess again you have {guess_count} chances left:  "))
    else:
        guess=int(input(f"No dear! Your number is higher Guess again you have {guess_count} chances left:  "))


print(f"Congrats {name}!!!\nYour Guess is correct:)\nYou guessed the answer in {guess_count} chances")
