pearl_list = []
user_input = str(input("Enter first string: "))
if user_input.lower() == "pearl":
    pearl_list.append(user_input)
if user_input == "quit":
        print()
        print("Bye!")

while user_input != "quit":
    user_input = str(input("Enter next string: "))
    if user_input == "quit":
        print(f"{len(pearl_list)} pearls")
        print("Bye!")
        break
    if user_input.lower() == "pearl":
        pearl_list.append(user_input)
