def double_factorial(user_input):
    input_parity = user_input % 2
    factorial = 1

#even
    if input_parity == 0:
        for i in range(1, user_input + 1, 1):
            if i % 2 == 0:
                factorial *= i
        return factorial

#odd
    else:
        for i in range(1, user_input + 1, 1):
            if i % 2 == 1:
                factorial *= i
        return factorial

def main():
    for i in range(0, 10, 1):
        print(f"{i}!! = {double_factorial(i)}")

main()