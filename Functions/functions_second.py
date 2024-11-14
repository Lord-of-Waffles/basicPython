def print_rectangle(height, width):

    for i in range(0, height, 1):
        for i in range(0, width, 1):
            print("*", end='')
        print()


def main():
    height = int(input("Enter height: "))
    width = int(input("Enter width: "))

    print_rectangle(height, width)

main()