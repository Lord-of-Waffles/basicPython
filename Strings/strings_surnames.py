name_amount = int(input("How many surnames? "))
names = []

for i in range(0,name_amount,1):
    new_name = str(input("Enter a surname: "))
    names.append(new_name.capitalize())
names = list(set(names))
names.sort()
print()
print(*names, sep=' ')