user_string = str(input("Enter a string: "))
if len(set(user_string)) == len(user_string):
    print("No duplicates")
else:
    print("Contains duplicate(s)")