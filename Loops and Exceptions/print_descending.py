i = int(input ("Enter an integer: "))
sum = 0
if i > 0 :
    for i in range(i, 0, -1):
        sum += i
        print(i, end=' ')
    print()   
    print(f'The sum is {sum}')
else:
    print('Nothing to be printed')