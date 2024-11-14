def unique_integers():
    input_list = []
    for i in range(5):
        new_int = input("Enter an integer: ")
        input_list.append(new_int)
    new_set = set(input_list)
    sorted_unique_list = sorted(new_set)
    sorted_input_list = sorted(input_list)
    print(", ".join(map(str, sorted_unique_list)))
    print(", ".join(map(str, sorted_input_list)))

def main():
    unique_integers()

main()
