apples = int(input("How many apples? "))
children = int(input("How many children? "))
remainder = apples % children
print()
print(f"Each child will get {apples // children} apples.")
print(f"There will be {remainder} leftover apples.")