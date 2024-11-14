first = str(input("Enter first string: "))
second = str(input("Enter second string: "))
first = first.replace(" ", "")
second = second.replace(" ", "")

if "".join(sorted(first)) == "".join(sorted(second)):
    print("Same characters")
else:
    print("Different characters")

