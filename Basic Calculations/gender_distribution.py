femaleStudents = float(input("Enter the number of female students: "))
maleStudents = float(input("Enter the number of male students: "))


totalStudents = femaleStudents + maleStudents
femalePercent = 0
if femaleStudents > 0:
    femalePercent = (femaleStudents / totalStudents) * 100
malePercent = 0
if maleStudents > 0:
    malePercent = (maleStudents / totalStudents) * 100

print()
print(f"Female: {femalePercent:.1f} %")
print(f"Male: {malePercent:.1f} %")