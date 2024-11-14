def new_doubled_list(numbers):
    new_numbers = numbers.copy()
    for i in range(0, len(new_numbers), 1):
        new_numbers[i] = new_numbers[i] * 2
    return new_numbers    

def main():
    first_list = [1, 2, 3, 4, 5, 6]
    second_list = new_doubled_list(first_list)
    print(first_list)
    print(second_list)
main()