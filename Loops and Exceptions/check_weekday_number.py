try:
    usernumber = int(input("Enter a weekday number: "))
    if usernumber <= 0:
        print("Please enter an integer between 1 and 7")
    elif usernumber > 7:
        print("Please enter an integer between 1 and 7")
    else:
        print("OK")
except ValueError:
    print("Please enter an integer between 1 and 7")




