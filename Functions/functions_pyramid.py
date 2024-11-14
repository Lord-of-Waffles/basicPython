def print_pyramid(height):
    tracker = 0
    for i in range(1, height + 1, 1):
        if i != height:
            print((height - i) * ' ' + (i + tracker) * '*')
            tracker = tracker + 1
        else:
            print((i + tracker) * '*')
            tracker = tracker + 1



def main():
    height = int(input("Enter pyramid height: "))
    return print_pyramid(height)

main()