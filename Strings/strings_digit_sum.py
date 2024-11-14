user_input = str(input("Enter a string: "))
numbers = []

for i in range(0,len(user_input), 1):

    if user_input[i].isdigit() == True:
        numbers.append(int(user_input[i]))
print(f"The sum of digits is {sum(numbers)}")