user_input = str(input("Enter a string: "))
for i in range(1, len(user_input)+1, 1):
    printable = user_input[0:i]
    if printable != 0:
        print(printable)