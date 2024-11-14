sellingPrice = float(input("Enter the car's selling price: "))
bonus = 0.015
if sellingPrice < 50000:
    bonus = 0.01
minimumBonus = 200
finalBonus = 0
if sellingPrice * bonus < minimumBonus:
    finalBonus = minimumBonus
else:
    finalBonus = sellingPrice * bonus
print(f"The bonus is {finalBonus:.2f} euros.")