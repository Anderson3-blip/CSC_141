name_prompt = "what's your name?"
place_prompt = "if you could visit one place in the world, where would it be?"
continue_prompt = "\nWould you like to let someones else respond (yes/no)"

# Responses will be stored in the form {name:place}.
responses = {}

while True:
    # Ask the user where they'd like to go.
    name = input(name_prompt)
    place = input(place_prompt)

    # store the response.
    responses[name] = place

    # anyone else
    repeat = input(continue_prompt)
    if repeat != 'yes':
        break


# results
print("\n---Results ---")
for name, place in responses.items():
    print(f"{name.title()} would like to visit {place.title()}.")