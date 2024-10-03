# Make an empty list to store people in

people = []

# define some people, and add to list
person = {
    'first_name' : 'eric',
    'last_name' : 'matthes',
    'age': 46,
    'city' : 'sitka',
    }

people.append(person)

person = {
    'first_name' : 'willie',
    'last_name' : 'matthes',
    'age' : 11,
    'city' : 'sitka',
    }

people.append(person)


# display all

for person in people:
    name = f"{person['first_name'].title()} {person['last_name'].title}"
    age = person['age']
    city = person['city'].title()

    print(f"{name}, of {city}, is {age} years old.")