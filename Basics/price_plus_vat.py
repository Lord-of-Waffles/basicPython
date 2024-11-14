

try:
    price = float(input("Enter price: "))
    VAT = 0.24
    pricePlusVAT = price * (1 + VAT)
    print(f"The price with VAT is {pricePlusVAT:.2f}")
except ValueError:
    print("Invalid price")


