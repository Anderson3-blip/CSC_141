def make_sandwich(*items):
    """make sandwich with the given items."""
    print("\nI'll make you a great sandwich:")
    for item in items:
        print(f"...adding {item} to your sandwich.")
        print("Your sandwich is ready!")


make_sandwich('peanut butter')
make_sandwich('roast beef','cheese')
make_sandwich('turkey','ham')