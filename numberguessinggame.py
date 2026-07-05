import random

print("Welcome to NUMBER GUESSING GAME")
print("I am thinking of a number between 1 and 20")

secret_number = random.randint(1, 20)

for chance in range(1, 6):
    guess = int(input("Take a guess: "))
    
    if guess < secret_number:
        print("Your guess is too low")
    elif guess > secret_number:
        print("Your guess is too high")
    else:
        print("Wow You guessed it right")
        print("You won the game")
        break
else:
    print("Game Over")
