guests = ['Cristiano Ronaldo', 'John Cena', 'Kawhi Leonard']

name = guests[0].title()
print(f"{guests}, will you please come to dinner.")

name = guests[1].title()
print(f"{guests}, will you please come to dinner.?")

name = guests[2].title()
print(f"{guests}, will you please come to dinner.?")

name = guests[1].title()
print(f"\nSorry, {guests[2]} can't make it to dinner.")

# Kawhi can't make it! Let's invite Ronaldo.
del(guests[1])
guests.insert(1, 'Cristiano Ronaldo')

# Print the invitations again.
name = guests[1].title()
print(f"\n{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")



# we have a bigger table with more guest
guests.insert(0, 'The Rock')
guests.insert(2, 'Romain Reigns')
guests.append('Virgil Van Djik')

name = guests[0].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")

name = guests[3].title()
print(f"{name}, please come to dinner.")

name = guests[4].title()
print(f"{name}, please come to dinner.")

name = guests[5].title()
print(f"{name}, please come to dinner.")

print("\nSorry, we can only invite two people to dinner.")

name = guests.pop()
print(f"Sorry, {name.title()} there's no room at the table.")

name = guests.pop()
print(f"Sorry, {name.title()} there's no room at the table.")

name = guests.pop()
print(f"Sorry, {name.title()} there's no room at the table.")

name = guests.pop()
print(f"Sorry, {name.title()} there's no room at the table.")

# There should be two people left. Let's invite them.
name = guests[0].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")




del(guests[0])
del(guests[0])
print(guests)