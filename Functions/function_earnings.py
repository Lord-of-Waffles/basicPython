def compute_earnings(wage, hours):
    if hours > 40:
        overtime = hours - 40
        salary = (hours - overtime) * wage
        bonus_wage = wage * 1.5
        bonus = overtime * bonus_wage
        return salary + bonus
    else:
        salary = hours * wage
        return salary

def main():
    wage = float(input("Enter wage: "))
    hours = int(input("Enter hours: "))

    return compute_earnings(wage, hours)

print(f"The earnings are {main():.2f}")