motorcycles = ['ducati', 'Aprilia', 'honda']
print(motorcycles)


motorcycles[0]='Aprilia'
print(motorcycles)



motorcycles.append('Aprialia')
print(motorcycles)



motorcycles.insert(0,'Honda')
print(motorcycles)


del motorcycles[4]
print(motorcycles)


popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)


last_owned = motorcycles.pop()
print(f"The last motorcycle i owned was a {last_owned.title()}.")


first_owned = motorcycles.pop(0)
print(f"The first motorcycle i owned was a {first_owned.title()}.")



motorcycles = ['Aprilia, Honda,Ducati']
print(motorcycles)





too_expensive = 'Aprilia'
print(motorcycles)
print(f"\nA {too_expensive.title()}is too expensive for me.")