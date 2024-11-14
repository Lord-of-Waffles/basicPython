user_string = str(input("Enter a string: "))
user_char = str(input("Enter a character: "))
for i in range(0, len(user_string), 1):
    if user_string[i] == user_char[0]:
        if len(user_string[i:i+4]) == 4:
            print(user_string[i:i+4])