prompt = "\nTell me something, and i will repeat it back to you:"
prompt += "\nEnter 'quit' to end program."

message = ""
while message != 'quit':
    message = input(prompt)
    print(message)





active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)