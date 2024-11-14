sum = 0
counter = 0
x = float(input('Enter first number: '))
if x == 0:
    print("Nothing to be calculated")
else:
    while  x != 0:
        sum = sum + x
        counter +=1
        x = float(input('Enter next number: '))
    average = sum/counter
    print(f"The average is {average:.2f}")