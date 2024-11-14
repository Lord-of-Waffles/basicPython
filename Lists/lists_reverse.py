int_amount = int(input("How many integers? "))
int_list = []
for i in range(0, int_amount, 1):
    new_int = int(input("Enter an integer: "))
    int_list.append(new_int)
print()
int_list.reverse()
print(*int_list)