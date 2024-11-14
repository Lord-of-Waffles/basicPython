user_input = str(input("Enter a string: "))
is_palindrome = False
if user_input == user_input[::-1]:
    is_palindrome = True
if is_palindrome == True:
    print("Yes")
else:
    print("No")