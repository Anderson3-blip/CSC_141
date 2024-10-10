seating_size = input("How many people are in your dinner party tonight?")
seating_size = int(seating_size)

if seating_size > 8:
    print("I'm sorry, you'll have to wait for a table.")
else:
    print("Your table is ready.")