int_list = []
for i in range(0, 5, 1):
    user_input = int(input("Enter an integer: "))
    int_list.append(user_input)

print(f"count: {len(int_list)}")
print(f"min:   {min(int_list)}")
print(f"max:   {max(int_list)}")
print(f"sum:   {sum(int_list)}")