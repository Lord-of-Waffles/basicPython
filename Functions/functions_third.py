def compute_discount(price, discount):
    discount_amount = price * discount
    return discount_amount


def main():
    price = float(input("Enter price: "))
    discount = float(input("Enter discount percentage: "))
    discount = discount / 100
    return compute_discount(price, discount)

print(f"The discount is {main():.2f} euros")