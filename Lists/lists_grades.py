
grade_list =["A", "A", "B", "A", "C", "B", "C", "F", "B", "B", "A", "A", "C", "C", "C"]
user_input = str(input("Enter grade letter: "))

if grade_list.count(user_input) != 0:
    total_amount = len(grade_list)
    grade_amount =  grade_list.count(user_input)
    percentage = (grade_amount / total_amount) * 100
    print(f"{percentage:.1f} %")
else:
    print("0.0 %")

