
interest = float(input("Enter interest rate: "))
tax = float(input("Enter capital income tax rate: "))
deposit = float(input("Enter initial deposit: "))
years = int(input("Enter number of years: "))

print()

for i in range(1, years + 1 , 1):
    interestamount = deposit * (interest / 100.0)
    taxamount = interestamount - (interestamount * (tax / 100.0))
    deposit = deposit + taxamount
    print(f"Year {i}: {deposit:.2f}")
