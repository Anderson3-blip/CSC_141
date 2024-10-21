#Battle ship 
#Regular frame work, we're gonna editm it to our liking 
import random

def battleship_game():
    print("Welcome to Battleship!")
    print("Choose a number between 1-10")
    
    ship_location = random.randint(1, 10),
    attempts = 0
    
    while True:
        guess = input("Enter your number 1-10: ")
        
        # Validate the input
        if not guess.isdigit() or not (1 <= int(guess) <= 10):
            print("please enter a  number between 1 and 10.")
            continue
        
        guess = int(guess)
        attempts += 1
        
        if guess == ship_location:
            print("Too low! Try again.")
        elif guess == ship_location:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You sunk my battleship in {attempts} try's !")
            break

battleship_game()