def positive_sum(inputs):
    sum = 0
    for i in range (0, len(inputs), 1):
        if inputs[i] > 0:
            sum += inputs[i]
    if sum == 0:
        return 0
    else:
        return sum



def main():
    inputs = []
    for i in range(0, 5, 1):
        user_input = int(input("Enter an integer: "))
        inputs.append(user_input)
    print()
    print(positive_sum(inputs))

main()