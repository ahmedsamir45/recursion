def fact(n):
    if n == 0:
        return 1
    result = n*fact(n-1)
    return result

again='k'
while again=='k':
    x =int(input('enter high index number to compination  : '))
    y =int(input('enter low index number to compination  : '))

    print('your compination : ', fact(x)/(fact(y)*fact(x-y)))
    again=input('do you want to calculate another compination (enter k for yes): ')
