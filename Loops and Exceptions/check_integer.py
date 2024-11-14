try:
    input = input("Enter an integer: ")
    input = int(input)
    print('OK')
except ValueError:
    print(f"'{input}' is not an integer")