gigs = int(input("Number of gigs: "))
gigsSame = float(input("Gigs to be played with the same set of strings: "))
price = float(input("Price of a set of guitar strings: "))
stringAmount = 0;
totalCost = 0;
if gigs == 1:
    stringAmount = 1
    totalCost = price
    print(f"The guitarist needs {stringAmount:.0f} new sets of guitar strings")
    print(f"The total cost is {totalCost:.2f} euros")
elif gigs == 0:
    print(f"The guitarist needs {stringAmount:.0f} new sets of guitar strings")
    print(f"The total cost is {totalCost:.2f} euros")
elif gigs > 1:
    stringAmount = int(gigs/gigsSame) + (gigs % gigsSame >0)
    #gigs/gigsSame
    totalCost = round(stringAmount) * price
    print(f"The guitarist needs {stringAmount:.0f} new sets of guitar strings")
    print(f"The total cost is {totalCost:.2f} euros")



