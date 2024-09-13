
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








