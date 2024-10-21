import random

def battleship_game():
    print("Welcome to 2 Player battleship!")
    print("Both players are given a random number between 1-20 each player must choose a number to hit the other player's ship to win.")

    # ship locations for both players
    ship_location = random.randint(1, 20)
    player2_ship_location = random.randint(1, 20)
    attempts = 0
    opponent_attempts = 0

    while True:
        
        guesses = input("Enter your number (1-20), Player 1: ")
        
        
        if not guesses.isdigit() or not (1 <= int(guesses) <= 20):
            print("Enter a number between 1 and 20.")
            continue
        
        guess = int(guesses)
        attempts += 1
        
        if guess < ship_location:
            print("Too low, try again.")
        elif guess > ship_location:
            print("Too high, try again.")
        else:  # If player number 1 wins
            print(f"Player 1, congratulations! ou sunk Player 2's battleship in {attempts} tries!")
            break  
        
        # 2's turn
        opponent_guesses = input("Enter your number (1-20), Player 2: ")

        # player 2's input
        if not opponent_guesses.isdigit() or not (1 <= int(opponent_guesses) <= 20):
            print("Enter a number between 1 - 20.")
            continue
        
        opponent_guess = int(opponent_guesses)
        opponent_attempts += 1

        if opponent_guess < player2_ship_location:
            print("Too low, try again.")
        elif opponent_guess > player2_ship_location:
            print("Too high, try again.")
        else:  
            print(f"Player 2, congratulations! You sunk Player 1's battleship in {opponent_attempts} tries!")
            break  # Exit the loop if Player 2 wins

battleship_game()