def pow_2_3(x):
    result_tuple = (x*x, x*x*x)
    return result_tuple

def main():
    x = int(input("Enter an integer: "))
    p2, p3 = pow_2_3(x)
    print(p2)
    print(p3)
if __name__ == "__main__":
    main()