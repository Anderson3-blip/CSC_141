import random

# Create the 5x5 grid for ships
GRID_SIZE = 5

# Create different ship sizes for both player and AI
PLAYER_SHIPS = {'Destroyer': 2, 'Submarine': 3, 'Battleship': 4}
AI_SHIPS = {'Destroyer': 2, 'Submarine': 3, 'Battleship': 4}

def place_ships(ship_sizes):
    """Randomly place ships on the grid, making sure they don't overlap."""
    ship_positions = []
    
    for ship, size in ship_sizes.items():
        while True:
            # Randomly choose orientation and start position
            orientation = random.choice(['H', 'V'])
            if orientation == 'H':
                start_row = random.randint(0, GRID_SIZE - 1)
                start_col = random.randint(0, GRID_SIZE - size)
                positions = [(start_row, start_col + i) for i in range(size)]
            else:
                start_row = random.randint(0, GRID_SIZE - size)
                start_col = random.randint(0, GRID_SIZE - 1)
                positions = [(start_row + i, start_col) for i in range(size)]
            
            # Check if positions overlap with existing ships
            if all(pos not in ship_positions for pos in positions):
                ship_positions.extend(positions)
                break
    
    return ship_positions

def battleship_game():
    print("Welcome to Battleship!")
    print("Sink the enemy fleet before they sink yours!")
    
    # Place ships for both player and AI
    player_ship_positions = place_ships(PLAYER_SHIPS)
    ai_ship_positions = place_ships(AI_SHIPS)
    
    player_hits = 0
    ai_hits = 0
    total_player_ships = sum(PLAYER_SHIPS.values())
    total_ai_ships = sum(AI_SHIPS.values())
    attempts = 0
    max_attempts = 20  # Limited ammunition to make it competitive
    died_once = False

    def print_grid():
        """Print the grid with markers for guesses."""
        print("  1 2 3 4 5")
        for row in range(GRID_SIZE):
            row_string = f"{row+1} "
            for col in range(GRID_SIZE):
                row_string += ". "
            print(row_string)

    # Game loop
    while player_hits < total_ai_ships and ai_hits < total_player_ships and attempts < max_attempts:
        print_grid()
        guess = input("Enter your target (e.g., 3 4 for row 3, column 4): ")
        
        try:
            row, col = map(int, guess.split())
            row -= 1
            col -= 1
            
            if not (0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE):
                print("Please enter valid grid coordinates.")
                continue
        except ValueError:
            print("Invalid input format. Use row and column numbers (e.g., 3 4).")
            continue

        attempts += 1

        # Check if player hit an AI ship
        if (row, col) in ai_ship_positions:
            player_hits += 1
            ai_ship_positions.remove((row, col))
            print(f"Hit! You sunk part of the enemy's fleet!")
        else:
            print("Miss! Try again.")

        # AI randomly guesses a spot to target player ships
        ai_guess = (random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1))
        if ai_guess in player_ship_positions:
            ai_hits += 1
            player_ship_positions.remove(ai_guess)
            print(f"Enemy hit your ship at {ai_guess[0]+1}, {ai_guess[1]+1}!")

        # Random chance for the player to hit a mine and "die"
        if not died_once and random.choice([True, False]):
            print("You hit a mine and died! You lost this round.")
            died_once = True

        print(f"Player hits: {player_hits}/{total_ai_ships}, Enemy hits: {ai_hits}/{total_player_ships}, Attempts left: {max_attempts - attempts}")

    # Determine the winner
    if player_hits >= total_ai_ships:
        print("Congratulations! You sunk all enemy ships!")
    elif ai_hits >= total_player_ships:
        print("The enemy sunk all your ships! You lost.")
    else:
        print("Out of ammunition! It's a draw.")
    
    if died_once:
        print("Remember, you died once from hitting a mine!")

battleship_game()
