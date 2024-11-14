user_input = str(input("Enter a string: "))
if len(user_input) < 2:
    print("Too short string")
else:
    print(user_input[len(user_input) - 2])