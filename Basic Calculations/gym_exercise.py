visits = int(input("Enter the number of days of gym visits per year: "))
passPrice = float(input("Enter price for a day pass: "))
yearFee = float(input("Enter yearly membership fee: "))
print()
dayPassPrice = visits * passPrice
if yearFee < dayPassPrice:
    yearPrice = dayPassPrice - yearFee
    print(f"Paying the yearly membership fee is {yearPrice:.2f} euros cheaper")
elif dayPassPrice < yearFee:
    dayPrice = yearFee - dayPassPrice
    print(f"Buying day passes is {dayPrice:.2f} euros cheaper")
else:
    print("There is no price difference")