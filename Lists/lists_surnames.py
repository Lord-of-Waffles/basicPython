user_input =''
names = []
while user_input != 'ok':
    user_input = input('Enter a surname (ok ends): ')
    if user_input != 'ok':
        names.append(user_input)
names = list(set(names))
names.sort()
print()
if len(names) > 1:
    print(*names, sep=", ")
else:
    print(*names)