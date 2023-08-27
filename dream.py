def dream(x):
    if x==0:
        return
    print('Dream')
    dream(x-1)

    
n = int(input('enter number for print dream : '))

dream(n)
