int_list = []
for i in range(0, 5, 1):
    user_input = int(input("Enter an integer: "))
    int_list.append(user_input)
print()
int_list.sort()
int_list.reverse()
for i in range(0, 5, 1):
    print(int_list[i], end=' ')