favorite_pizzas = ['Sausage', 'veggie','pepperoni']
friend_pizzas = favorite_pizzas[:]

favorite_pizzas.append("sausage lover")
friend_pizzas.append('pepper')

print("My favorite pizzas are:")
for pizza in favorite_pizzas :
    print(f"-{pizza}")

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(f"-{pizza}")