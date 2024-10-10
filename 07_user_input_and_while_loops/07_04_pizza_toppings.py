prompt = "\n what topping would you like on your pizza?"
prompt += "\nEnter 'quit' when you are finished:"

while True:
    topping = input(prompt)
    if topping != 'quit':
        print(f"i'll add {topping} to your pizza.")
    else:
        break 