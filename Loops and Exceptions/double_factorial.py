user_input = int(input("Enter a non-negative integer: "))
if user_input < 0:
    print("Please enter a non-negative integer")

input_parity = user_input % 2
factorial = 1

#even
if input_parity == 0:
    for i in range(1, user_input + 1, 1):
        if i % 2 == 0:
            factorial *= i

#odd
else:
    for i in range(1, user_input + 1, 1):
        if i % 2 == 1:
            factorial *= i
            
print(f"{user_input}!! = {factorial}")