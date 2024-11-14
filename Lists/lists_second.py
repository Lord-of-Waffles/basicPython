list = []
user_input = ''
while user_input != 'quit':
    user_input = input("Enter a word (quit ends): ")
    if user_input != 'quit':
        list.append(user_input)

list.sort()

print(*list, sep='\n')