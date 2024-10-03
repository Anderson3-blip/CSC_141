favorite_number = {
    'john' : [23, 17],
    'gru' : [18,39, 54],
    'bron': [21,3],
    }

for name, numbers in favorite_number.items():
    print(f"\n{name.title()} likes the following numbers:")
    for number in numbers:
        print(f"  {number}")