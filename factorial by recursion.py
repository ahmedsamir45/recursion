def fact(n):
    if n == 0:
        return 1
    result = n*fact(n-1)
    return result

again='k'
while again=='k':
    x =int(input('enter number to get factorial : '))

    print('your fact : ', fact(x))
    again=input('do you want to calculate another factorial (enter k for yes): ')
