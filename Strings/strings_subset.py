first = str(input("Enter first string: "))
second = str(input("Enter second string: "))
subset = True
if len(second) == 0:
    print('Nothing to be checked')
for i in range(0,len(second), 1):
    if second[i].lower() in first.lower():
        subset = True
    else:
        subset = False
        break

if subset == True:
    print('Subset')
else:
    print('Not subset')