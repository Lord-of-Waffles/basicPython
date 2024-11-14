isdone = 0
while isdone == 0:
    try:
        x = input("Enter a month number: ")
        x = int(x)
        if x <= 0:
            print(f"{x} is not a valid month number") 
            print()
        elif x > 12:
            print(f"{x} is not a valid month number") 
            print()
        else:
            print("OK")
            isdone = 1
    except ValueError:
        print(f"'{x}' is not a valid month number")
        print()