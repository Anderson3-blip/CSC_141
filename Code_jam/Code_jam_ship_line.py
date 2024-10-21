#Battle Ship
#Updated version but with dying atleast once
import random

def battleship_game():
    print("Welcome to Battleship!")
    print("There are 4 hidden ships! Try to sink them all by guessing their locations.")
    print("Choose numbers between 1 and 10.")
    
    # Generate 4 random ship locations, ensuring no duplicates
    ship_locations = random.sample(range(1, 11), 4)
    attempts = 0
    ships_sunk = 0
    died_once = False
    
    while ships_sunk < 4:
        guess = input("Enter your number (1-10): ")
        
        # Validate the input
        if not guess.isdigit() or not (1 <= int(guess) <= 10):
            print("Please enter a valid number between 1 and 10.")
            continue
        
        guess = int(guess)
        attempts += 1
        
        # Random chance to "die"
        if not died_once and random.choice([True, False]):
            print("Oh no! You hit a mine and died. You lost this round!")
            died_once = True
            continue  # The game continues, but you "died" once
        
        # Check if the guess hits a ship
        if guess in ship_locations:
            ship_locations.remove(guess)
            ships_sunk += 1
            print(f"Hit! You've sunk {ships_sunk} ship(s)!")
        else:
            print("Miss! Try again.")
    
    print(f"Congratulations! You sunk all the ships in {attempts} attempts.")
    if died_once:
        print("But remember, you died once!")
    else:
        print("You managed to survive without dying!")
    
battleship_game()
