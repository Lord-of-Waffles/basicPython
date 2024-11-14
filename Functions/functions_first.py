def print_powers():

    x = 1
    for i in range (1, 21):

        print(x, end=' ')
        x = x * 2
        if x == 1:
            x = 2

def main():
    print_powers()
main()